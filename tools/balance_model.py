"""Monte Carlo balance model for Stew's Game.

Models the rules at the level of money and stats so the dials can be set before
any perk or tile content gets authored. Nothing here is game code.

Action tile mechanic (docs/03): each action tile offers two life choices. One is
the "good" action and raises a stat by a fixed X, usually at a money cost. The
other is the "bad" action and lowers a stat by the same X, usually free or
paying out. Movement is symmetric by construction and expected drift is zero.

  "Train for a half marathon, pay $X"  ->  Brawn +10, cost
  "Snacktime on the couch"             ->  Brawn -10, free

Most tiles put both options on the same stat; some trade one stat against
another.

Usage:  py tools/balance_model.py [--runs 8000] [--seed 7]
"""

from __future__ import annotations

import argparse
import math
import random
import statistics
from dataclasses import dataclass, field

ALL_STATS = ("brains", "brawn", "buds", "bliss", "bravado")
TIERS = (25, 50, 75, 100)
STAT_CAP = 100


# --------------------------------------------------------------------------
# Tunable design parameters. These are the dials.
# --------------------------------------------------------------------------

@dataclass
class Config:
    # Three stats today, reworked down from five. May grow again.
    stat_count: int = 3

    # Board shape (docs/03). Landings are derived, because turn count is what
    # actually drives both stat depth and async game duration.
    board_tiles: int = 72
    spinner_avg: float = 3.5
    salary_spacing: int = 6
    life_event_stops: int = 6
    action_share: float = 0.60      # of non-event landings

    # Action tiles (docs/02)
    delta_x: int = 10               # fixed magnitude of every stat change
    same_stat_share: float = 0.70   # both options move the same stat
    stat_up_cost: int = 12_000      # price of the virtuous option
    stat_down_gain: int = 6_000     # payout of the indulgent option
    event_delta: tuple[int, int] = (10, 20)
    stat_life_events: int = 3
    start_points: int = 0

    # Economy (docs/05)
    start_cash: int = 25_000
    salary_band: dict[int, int] = field(
        default_factory=lambda: {1: 30_000, 2: 45_000, 3: 62_000}
    )
    senior_mult: float = 1.5
    exec_mult: float = 2.2
    senior_frac: float = 0.25       # of expected paydays
    exec_frac: float = 0.55
    tuition: dict[str, int] = field(
        default_factory=lambda: {"none": 0, "undergrad": 80_000, "grad": 160_000}
    )
    tier_by_path: dict[str, int] = field(
        default_factory=lambda: {"none": 1, "undergrad": 2, "grad": 3}
    )
    # Education costs tiles, not a flat number of paydays.
    education_tiles: dict[str, int] = field(
        default_factory=lambda: {"none": 0, "undergrad": 6, "grad": 12}
    )

    # Outcome tiles
    outcome_money: tuple[int, int] = (5_000, 40_000)
    outcome_karma: tuple[int, int] = (-8, 8)

    # Investments (docs/05)
    invest_returns: tuple[float, ...] = (-0.10, -0.04, 0.03, 0.06, 0.12, 0.22)
    cash_buffer: int = 60_000

    # Marriage (docs/04). Spec: spouse adds 50% salary, all costs double.
    marriage_salary_share: float = 0.5
    double_all_costs: bool = True

    # Loans (docs/05)
    loan_interest: float = 0.20
    loan_karma: int = -5

    # Layoffs (docs/04)
    layoff_base: float = 0.05
    layoff_divisor: float = 40.0
    layoff_floor: float = 0.005
    layoff_ceiling: float = 0.12

    # Houses (docs/05)
    houses: tuple[tuple[int, int, int], ...] = (
        (120_000, 100_000, 180_000),
        (250_000, 200_000, 380_000),
        (450_000, 350_000, 700_000),
    )

    # Life event costs (docs/04)
    birth_cost: int = 40_000
    adoption_cost: int = 120_000
    adoption_karma: int = 15
    crisis_cost: tuple[int, int] = (60_000, 200_000)

    # Scoring (docs/05)
    score_mode: str = "net"
    pos_tier_mult: float = 0.12
    neg_tier_value: int = 6_000
    karma_to_score: int = 2_000
    child_score: int = 150_000
    prestige_score: dict[int, int] = field(
        default_factory=lambda: {1: 0, 2: 40_000, 3: 90_000}
    )

    # --- Derived shape ----------------------------------------------------

    def turns(self, education: str = "none") -> int:
        tiles = self.board_tiles + self.education_tiles[education]
        return max(1, round(tiles / self.spinner_avg))

    def paydays(self, education: str = "none") -> int:
        # Education tiles are off the main path, so they cost paydays.
        spent = self.education_tiles[education] / self.spinner_avg
        base = self.board_tiles / self.salary_spacing
        return max(1, round(base - spent))

    def action_landings(self, education: str = "none") -> int:
        free = max(0, self.turns(education) - self.life_event_stops)
        return round(free * self.action_share)

    def outcome_landings(self, education: str = "none") -> int:
        free = max(0, self.turns(education) - self.life_event_stops)
        return free - self.action_landings(education)


@dataclass
class Policy:
    """How an archetype plays."""
    name: str
    direction: int              # +1 always the good option, -1 always the bad
    education: str = "undergrad"
    married: bool = False
    children: int = 0


def stat_names(cfg: Config) -> tuple[str, ...]:
    return ALL_STATS[:cfg.stat_count]


def _tiers_held(value: int, direction: int) -> int:
    if direction > 0:
        return sum(1 for t in TIERS if value >= t)
    return sum(1 for t in TIERS if value <= -t)


def _resolve_action_tile(rng: random.Random, cfg: Config, policy: Policy,
                         stats: dict[str, int], names: tuple[str, ...]):
    """Returns the cash effect of the choice. Mutates stats."""
    direction = policy.direction or rng.choice((-1, 1))

    if rng.random() < cfg.same_stat_share:
        target = rng.choice(names)
    else:
        up, down = rng.sample(names, 2)
        target = up if direction > 0 else down

    stats[target] = max(-STAT_CAP, min(STAT_CAP,
                                       stats[target] + direction * cfg.delta_x))
    return -cfg.stat_up_cost if direction > 0 else cfg.stat_down_gain


# --------------------------------------------------------------------------
# One simulated run
# --------------------------------------------------------------------------

def simulate(rng: random.Random, cfg: Config, policy: Policy) -> dict:
    names = stat_names(cfg)
    stats = {s: 0 for s in names}
    if cfg.start_points:
        stats[names[0]] = cfg.start_points * (policy.direction or 1)

    paydays = cfg.paydays(policy.education)
    n_action = cfg.action_landings(policy.education)
    n_outcome = cfg.outcome_landings(policy.education)

    cash = float(cfg.start_cash)
    invested = 0.0
    debt = 0.0
    karma = 0

    tuition = cfg.tuition[policy.education]
    if tuition:
        debt += tuition
        karma += cfg.loan_karma

    tier = cfg.tier_by_path[policy.education]
    base_salary = cfg.salary_band[tier]
    senior_at = max(1, round(paydays * cfg.senior_frac))
    exec_at = max(2, round(paydays * cfg.exec_frac))
    career_paydays = 0

    def pay_cost(amount: float, involuntary: bool) -> None:
        nonlocal cash, debt, karma
        if policy.married and (involuntary or cfg.double_all_costs):
            amount *= 2
        if cash >= amount:
            cash -= amount
        else:
            # Invested money is one turn away, so a shortfall means a loan.
            debt += amount - cash
            cash = 0.0
            karma += cfg.loan_karma

    house_payday = max(1, round(paydays * 0.39))
    child_paydays = {max(1, round(paydays * f)) for f in (0.47, 0.61)}
    crisis_payday = max(1, round(paydays * 0.69))
    event_paydays = {max(1, round(paydays * f)) for f in (0.3, 0.5, 0.7)}

    per_payday_action = n_action / paydays
    per_payday_outcome = n_outcome / paydays
    action_debt = outcome_debt = 0.0

    house_sale = 0
    children = 0

    for payday in range(1, paydays + 1):
        if career_paydays >= exec_at:
            salary = base_salary * cfg.exec_mult
        elif career_paydays >= senior_at:
            salary = base_salary * cfg.senior_mult
        else:
            salary = base_salary
        if policy.married:
            salary *= 1 + cfg.marriage_salary_share
        cash += salary
        career_paydays += 1

        # Negative perks pay out during the run.
        neg_now = sum(_tiers_held(v, -1) for v in stats.values())
        cash += neg_now * cfg.neg_tier_value

        social = stats["brains"] + stats["buds"]
        chance = cfg.layoff_base - social / cfg.layoff_divisor / 100
        chance = max(cfg.layoff_floor, min(cfg.layoff_ceiling, chance))
        if rng.random() < chance:
            career_paydays = 0
            base_salary = cfg.salary_band[tier]

        # Action tiles landed on since the last payday.
        action_debt += per_payday_action
        while action_debt >= 1:
            action_debt -= 1
            effect = _resolve_action_tile(rng, cfg, policy, stats, names)
            if effect >= 0:
                cash += effect
            else:
                pay_cost(-effect, involuntary=False)

        outcome_debt += per_payday_outcome
        while outcome_debt >= 1:
            outcome_debt -= 1
            amount = rng.randint(*cfg.outcome_money)
            if rng.random() < 0.5:
                cash += amount
            else:
                pay_cost(amount, involuntary=True)
            karma += rng.randint(*cfg.outcome_karma)

        if payday in event_paydays:
            delta = rng.randint(*cfg.event_delta)
            target = rng.choice(names)
            step = delta * (policy.direction or rng.choice((-1, 1)))
            stats[target] = max(-STAT_CAP, min(STAT_CAP, stats[target] + step))

        if payday == house_payday:
            affordable = [h for h in cfg.houses if h[0] <= cash + invested * 0.5]
            if affordable:
                price, low, high = affordable[-1]
                pay_cost(price, involuntary=False)
                house_sale = rng.randint(low, high)

        if payday in child_paydays and children < policy.children:
            children += 1
            if rng.random() < 0.7:
                pay_cost(cfg.birth_cost, involuntary=True)
            else:
                pay_cost(cfg.adoption_cost, involuntary=True)
                karma += cfg.adoption_karma

        if payday == crisis_payday:
            cost = rng.randint(*cfg.crisis_cost)
            cost *= max(0.4, min(1.6, 1.0 - karma / 150))
            pay_cost(cost, involuntary=True)

        spare = cash - cfg.cash_buffer
        if spare > 0:
            cash -= spare
            invested += spare
        invested *= 1 + rng.choice(cfg.invest_returns)

    pos_tiers = sum(_tiers_held(v, +1) for v in stats.values())
    neg_tiers = sum(_tiers_held(v, -1) for v in stats.values())
    scoring_tiers = (max(0, pos_tiers - neg_tiers)
                     if cfg.score_mode == "net" else pos_tiers)

    net_worth = cash + invested + house_sale - debt * (1 + cfg.loan_interest)
    score = (
        net_worth * (1 + scoring_tiers * cfg.pos_tier_mult)
        + children * cfg.child_score
        + karma * cfg.karma_to_score
        + cfg.prestige_score[tier]
    )

    maxed = sum(1 for v in stats.values() if abs(v) >= STAT_CAP)
    return {
        "score": score,
        "net_worth": net_worth,
        "pos_tiers": pos_tiers,
        "neg_tiers": neg_tiers,
        "tiers": max(pos_tiers, neg_tiers),
        "peak_stat": max(abs(v) for v in stats.values()),
        "maxed_any": 1.0 if maxed >= 1 else 0.0,
        "maxed_all": 1.0 if maxed == cfg.stat_count else 0.0,
        "karma": karma,
        "debt": debt,
    }


def run(cfg: Config, policy: Policy, runs: int, seed: int) -> dict:
    rng = random.Random(seed)
    results = [simulate(rng, cfg, policy) for _ in range(runs)]
    out = {}
    for key in results[0]:
        values = [r[key] for r in results]
        out[key] = statistics.mean(values)
        out[key + "_sd"] = statistics.pstdev(values)
    out["scores"] = sorted(r["score"] for r in results)
    return out


def solve_parity(cfg: Config, runs: int, seed: int) -> float:
    """Positive tier multiplier that levels the two committed builds."""
    pos = Policy("committed positive", +1)
    neg = Policy("committed negative", -1)
    target = run(cfg, neg, runs, seed)["score"]
    lo, hi = 0.0, 2.0
    for _ in range(22):
        mid = (lo + hi) / 2
        probe = Config(**{**cfg.__dict__, "pos_tier_mult": mid})
        if run(probe, pos, runs, seed)["score"] < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


# --------------------------------------------------------------------------
# Reports
# --------------------------------------------------------------------------

def money(x: float) -> str:
    return f"${x/1000:,.0f}k"


def async_days(turns: int, players: int = 6, runs: int = 600) -> float:
    """Median async duration, via the pacing model."""
    try:
        from async_pacing import simulate as pace
    except ImportError:
        return float("nan")
    rng = random.Random(11)
    vals = sorted(pace(rng, players, turns, 24.0)["pipeline"]
                  for _ in range(runs))
    return statistics.median(vals) / 24.0


def finding_1_board_size(cfg: Config, runs: int, seed: int) -> None:
    print("=" * 78)
    print("FINDING 1 - How big does the board need to be to max a skill tree?")
    print("=" * 78)
    print("Maxing a stat at +/-100 needs 100/X landings that happen to hit it.")
    print("With 3 stats and random assignment, that's ~3x as many action")
    print("landings. Async duration is for 6 players, pipelined, 24h timeout.\n")
    print(f"{'tiles':>7} {'turns':>6} {'action':>7} {'paydays':>8} "
          f"{'peak':>6} {'tiers':>6} {'max 1':>7} {'max all':>8} "
          f"{'6p async':>9}")
    print("-" * 78)
    for tiles in (72, 120, 160, 200, 260, 320):
        trial = Config(**{**cfg.__dict__, "board_tiles": tiles})
        r = run(trial, Policy("p", +1), runs // 2, seed)
        t = trial.turns("undergrad")
        print(f"{tiles:>7} {t:>6} {trial.action_landings('undergrad'):>7} "
              f"{trial.paydays('undergrad'):>8} "
              f"{r['peak_stat']:>6.0f} {r['tiers']:>6.1f} "
              f"{r['maxed_any']:>6.0%} {r['maxed_all']:>7.0%} "
              f"{async_days(t):>8.1f}d")
    print()


def finding_2_delta_x(cfg: Config, runs: int, seed: int) -> None:
    print("=" * 78)
    print("FINDING 2 - Trading board size against the size of X")
    print("=" * 78)
    print("A bigger X reaches the same depth in fewer landings, so it buys")
    print("back calendar time. Showing the board size needed for most players")
    print("to max at least one stat, and what that costs in async days.\n")
    print(f"{'X':>4} {'tiles':>7} {'turns':>6} {'action':>7} {'peak':>6} "
          f"{'tiers':>6} {'max 1':>7} {'max all':>8} {'6p async':>9}")
    print("-" * 78)
    for x, tiles in ((5, 320), (10, 200), (15, 140), (20, 110), (25, 90)):
        trial = Config(**{**cfg.__dict__, "delta_x": x, "board_tiles": tiles})
        r = run(trial, Policy("p", +1), runs // 2, seed)
        t = trial.turns("undergrad")
        print(f"{x:>4} {tiles:>7} {t:>6} "
              f"{trial.action_landings('undergrad'):>7} "
              f"{r['peak_stat']:>6.0f} {r['tiers']:>6.1f} "
              f"{r['maxed_any']:>6.0%} {r['maxed_all']:>7.0%} "
              f"{async_days(t):>8.1f}d")
    print()


def finding_3_symmetry(cfg: Config, runs: int, seed: int) -> None:
    print("=" * 78)
    print("FINDING 3 - Is the negative path now symmetric?")
    print("=" * 78)
    print("The old mechanic moved stats down more slowly than up, so negative")
    print("builds could not reach their own perks. Symmetric +/-X should fix")
    print("that outright, and should also stop positive tiers leaking to")
    print("negative builds.\n")
    print(f"{'archetype':>22} {'peak':>6} {'own tiers':>10} "
          f"{'off-path tiers':>15}")
    print("-" * 78)
    p = run(cfg, Policy("p", +1), runs, seed)
    n = run(cfg, Policy("n", -1), runs, seed)
    print(f"{'committed positive':>22} {p['peak_stat']:>6.0f} "
          f"{p['pos_tiers']:>10.1f} {p['neg_tiers']:>15.1f}")
    print(f"{'committed negative':>22} {n['peak_stat']:>6.0f} "
          f"{n['neg_tiers']:>10.1f} {n['pos_tiers']:>15.1f}")
    print()
    sym = n["neg_tiers"] / p["pos_tiers"] if p["pos_tiers"] else 0
    print(f"  Negative depth is {sym:.0%} of positive depth "
          f"(was 43% under the old mechanic).")
    print(f"  Negative builds hold {n['pos_tiers']:.2f} stray positive tiers "
          f"(was 1.3), so the")
    print("  leak that made parity unsolvable is gone by construction.\n")


def finding_4_money_asymmetry(cfg: Config, runs: int, seed: int) -> None:
    print("=" * 78)
    print("FINDING 4 - The price of virtue is now the main balance lever")
    print("=" * 78)
    print("Good options cost money and bad options pay, so the negative path")
    print("earns its advantage through play rather than through perks. This")
    print("is the dial that decides how strong the gamble is.\n")
    print(f"{'up cost':>9} {'down gain':>10} {'cash swing':>12} "
          f"{'parity mult':>12} {'pos score':>11}")
    print("-" * 78)
    for up, down in ((4_000, 2_000), (8_000, 4_000), (12_000, 6_000),
                     (20_000, 10_000), (30_000, 15_000)):
        trial = Config(**{**cfg.__dict__, "stat_up_cost": up,
                          "stat_down_gain": down})
        required = solve_parity(trial, runs // 2, seed)
        tuned = Config(**{**trial.__dict__, "pos_tier_mult": required})
        r = run(tuned, Policy("p", +1), runs // 2, seed)
        swing = (up + down) * trial.action_landings("undergrad")
        print(f"{money(up):>9} {money(down):>10} {money(swing):>12} "
              f"{required:>11.1%} {money(r['score']):>11}")
    print()


def finding_5_archetypes(cfg: Config, runs: int, seed: int) -> None:
    print("=" * 78)
    print("FINDING 5 - Archetype spread at the tuned numbers")
    print("=" * 78)
    print(f"{'archetype':>24} {'mean score':>12} {'std dev':>10} "
          f"{'p10':>10} {'p90':>10}")
    print("-" * 78)
    for p in (Policy("committed positive", +1),
              Policy("committed negative", -1),
              Policy("uncommitted / drifting", 0)):
        r = run(cfg, p, runs, seed)
        s = r["scores"]
        print(f"{p.name:>24} {money(r['score']):>12} "
              f"{money(r['score_sd']):>10} "
              f"{money(s[len(s)//10]):>10} {money(s[9*len(s)//10]):>10}")
    print()


def finding_6_education(cfg: Config, runs: int, seed: int) -> None:
    print("=" * 78)
    print("FINDING 6 - Does education pay for itself?")
    print("=" * 78)
    print(f"{'path':>12} {'paydays':>8} {'turns':>6} {'mean score':>12} "
          f"{'vs no school':>13}")
    print("-" * 78)
    baseline = None
    for path in ("none", "undergrad", "grad"):
        r = run(cfg, Policy("balanced", +1, education=path), runs, seed)
        if baseline is None:
            baseline = r["score"]
        print(f"{path:>12} {cfg.paydays(path):>8} {cfg.turns(path):>6} "
              f"{money(r['score']):>12} {r['score']/baseline-1:>12.1%}")
    print()


def finding_7_family(cfg: Config, runs: int, seed: int) -> None:
    print("=" * 78)
    print("FINDING 7 - Marriage and children")
    print("=" * 78)
    single = run(cfg, Policy("s", +1), runs, seed)
    print(f"{'configuration':>26} {'mean score':>12} {'vs single':>11} "
          f"{'loans':>10}")
    print("-" * 78)
    print(f"{'single, no children':>26} {money(single['score']):>12} "
          f"{'--':>11} {money(single['debt']):>10}")
    for married, kids, label in ((True, 0, "married, no children"),
                                 (False, 2, "single, 2 children"),
                                 (True, 2, "married, 2 children")):
        r = run(cfg, Policy("x", +1, married=married, children=kids),
                runs, seed)
        print(f"{label:>26} {money(r['score']):>12} "
              f"{r['score']/single['score']-1:>10.1%} "
              f"{money(r['debt']):>10}")
    print()
    print("Child score value needed for children to be a real decision:")
    print("-" * 78)
    print(f"{'per child':>12} {'single, 2 kids':>16} {'vs childless':>14}")
    for value in (0, 75_000, 150_000, 225_000, 300_000):
        trial = Config(**{**cfg.__dict__, "child_score": value})
        s = run(trial, Policy("c", +1, children=2), runs, seed)["score"]
        print(f"{money(value):>12} {money(s):>16} "
              f"{s/single['score']-1:>13.1%}")
    print()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", type=int, default=8_000)
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--tiles", type=int, default=None)
    ap.add_argument("--x", type=int, default=None)
    args = ap.parse_args()

    cfg = Config()
    if args.tiles:
        cfg = Config(**{**cfg.__dict__, "board_tiles": args.tiles})
    if args.x:
        cfg = Config(**{**cfg.__dict__, "delta_x": args.x})

    print(f"\nStew's Game balance model - {args.runs:,} runs per cell, "
          f"seed {args.seed}")
    print(f"Board {cfg.board_tiles} tiles, X = {cfg.delta_x}, "
          f"{cfg.turns('undergrad')} turns, "
          f"{cfg.action_landings('undergrad')} action landings\n")

    finding_1_board_size(cfg, args.runs, args.seed)
    finding_2_delta_x(cfg, args.runs, args.seed)
    finding_3_symmetry(cfg, args.runs, args.seed)
    finding_4_money_asymmetry(cfg, args.runs, args.seed)

    required = solve_parity(cfg, args.runs, args.seed)
    cfg = Config(**{**cfg.__dict__, "pos_tier_mult": required})
    print(f"Solved positive tier multiplier: {required:.1%} per net tier\n")

    finding_5_archetypes(cfg, args.runs, args.seed)
    finding_6_education(cfg, args.runs, args.seed)
    finding_7_family(cfg, args.runs, args.seed)


if __name__ == "__main__":
    main()
