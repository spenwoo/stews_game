"""How long does an asynchronous multi-day game actually take?

Stew's Game is played over days, with players notified when it's their turn and
no meaningful shot clock. That removes the session-length problem but creates a
different one: wall-clock duration is driven by how often people open the app,
multiplied by how many turns the game contains.

Three turn-scheduling schemes are compared:

  strict    One player moves at a time, in fixed order. Total duration is the
            sum of every response latency in the game.
  pipeline  Fixed order preserved, but a player may take turn k as soon as
            their own turn k-1 and the previous player's turn k are done. So
            fast players run ahead while order is still respected.
  round     All players take their turn in a round in any order; the round
            advances when everyone has moved. Duration is the sum of per-round
            slowest responses.

Usage:  py tools/async_pacing.py [--runs 4000]
"""

from __future__ import annotations

import argparse
import random
import statistics

HOUR = 1.0
DAY = 24 * HOUR


def latency(rng: random.Random, timeout_h: float | None) -> float:
    """Hours until a notified player actually takes their turn.

    Modelled as a mixture, because async play is bimodal in practice: most
    turns happen soon after the notification, but some land after a night or a
    workday.
    """
    r = rng.random()
    if r < 0.45:
        v = rng.uniform(0.05, 1.0)        # saw the notification, played now
    elif r < 0.75:
        v = rng.uniform(1.0, 5.0)         # next break in the day
    elif r < 0.95:
        v = rng.uniform(8.0, 16.0)        # overnight or a full workday
    else:
        v = rng.uniform(20.0, 48.0)       # distracted / busy stretch
    return min(v, timeout_h) if timeout_h else v


def simulate(rng: random.Random, players: int, turns: int,
             timeout_h: float | None) -> dict[str, float]:
    lat = [[latency(rng, timeout_h) for _ in range(turns)]
           for _ in range(players)]

    strict = sum(sum(row) for row in lat)

    # pipeline: finish[i][k] = lat + max(own previous turn, previous player's
    # turn k). Players may run ahead of slower ones without breaking order.
    prev_player = [0.0] * turns
    for i in range(players):
        own = 0.0
        cur = []
        for k in range(turns):
            start = max(own, prev_player[k])
            own = start + lat[i][k]
            cur.append(own)
        prev_player = cur
    pipeline = prev_player[-1]

    rounds = sum(max(lat[i][k] for i in range(players)) for k in range(turns))

    return {"strict": strict, "pipeline": pipeline, "round": rounds}


def report(runs: int, seed: int, turns: int, timeout_h: float | None) -> None:
    label = f"{timeout_h:.0f}h auto-play timeout" if timeout_h else "no timeout"
    print("=" * 76)
    print(f"Expected wall-clock duration - {turns} turns per player, {label}")
    print("=" * 76)
    print(f"{'players':>8}  {'strict order':>22}  {'pipelined':>22}  "
          f"{'round-based':>22}")
    print(f"{'':>8}  {'median / p90':>22}  {'median / p90':>22}  "
          f"{'median / p90':>22}")
    print("-" * 76)

    for players in (2, 3, 4, 6):
        rng = random.Random(seed)
        res = [simulate(rng, players, turns, timeout_h) for _ in range(runs)]
        cells = []
        for key in ("strict", "pipeline", "round"):
            vals = sorted(r[key] for r in res)
            med = statistics.median(vals) / DAY
            p90 = vals[int(0.9 * len(vals))] / DAY
            cells.append(f"{med:>9.1f}d /{p90:>6.1f}d")
        print(f"{players:>8}  {cells[0]:>22}  {cells[1]:>22}  {cells[2]:>22}")
    print()


def report_turn_sensitivity(runs: int, seed: int) -> None:
    print("=" * 76)
    print("Board length vs. duration (6 players, round-based, 24h timeout)")
    print("=" * 76)
    print(f"{'board tiles':>12}  {'turns each':>11}  {'median':>9}  "
          f"{'p90':>8}  {'over 14 days':>13}")
    print("-" * 76)
    for tiles, turns in ((48, 14), (60, 17), (72, 21), (96, 27)):
        rng = random.Random(seed)
        vals = sorted(simulate(rng, 6, turns, 24.0)["round"]
                      for _ in range(runs))
        med = statistics.median(vals) / DAY
        p90 = vals[int(0.9 * len(vals))] / DAY
        over = sum(1 for v in vals if v > 14 * DAY) / len(vals)
        print(f"{tiles:>12}  {turns:>11}  {med:>8.1f}d  {p90:>7.1f}d  "
              f"{over:>12.0%}")
    print()


def report_timeout(runs: int, seed: int, turns: int) -> None:
    print("=" * 76)
    print("Does a generous auto-play timeout help? (6 players, round-based)")
    print("=" * 76)
    print(f"{'timeout':>12}  {'median':>9}  {'p90':>8}  {'turns auto-played':>19}")
    print("-" * 76)
    for timeout_h in (None, 48.0, 24.0, 12.0):
        rng = random.Random(seed)
        vals = sorted(simulate(rng, 6, turns, timeout_h)["round"]
                      for _ in range(runs))
        med = statistics.median(vals) / DAY
        p90 = vals[int(0.9 * len(vals))] / DAY
        # Share of turns that would hit the cap, from the mixture directly.
        rng2 = random.Random(seed + 1)
        sample = [latency(rng2, None) for _ in range(40_000)]
        auto = (sum(1 for v in sample if timeout_h and v > timeout_h)
                / len(sample))
        name = f"{timeout_h:.0f}h" if timeout_h else "none"
        print(f"{name:>12}  {med:>8.1f}d  {p90:>7.1f}d  {auto:>18.1%}")
    print()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", type=int, default=4000)
    ap.add_argument("--seed", type=int, default=11)
    ap.add_argument("--turns", type=int, default=21)
    args = ap.parse_args()

    rng = random.Random(args.seed)
    sample = [latency(rng, None) for _ in range(40_000)]
    print(f"\nLatency model: mean {statistics.mean(sample):.1f}h, "
          f"median {statistics.median(sample):.1f}h, "
          f"{sum(1 for v in sample if v < 1) / len(sample):.0%} within the hour\n")

    report(args.runs, args.seed, args.turns, 24.0)
    report(args.runs, args.seed, args.turns, None)
    report_turn_sensitivity(args.runs, args.seed)
    report_timeout(args.runs, args.seed, args.turns)


if __name__ == "__main__":
    main()
