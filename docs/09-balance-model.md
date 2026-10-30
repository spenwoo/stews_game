# 09 — Balance Model

Results from [`tools/balance_model.py`](../tools/balance_model.py), a Monte Carlo
model of the rules at the level of money and stats. Run it with:

```
py tools/balance_model.py --runs 20000
```

Figures below are from 6,000 runs per cell, seed 7. It's a model, not a
playtest — it assumes players execute a plan competently and makes no attempt to
model misplays. Treat the numbers as showing the *shape* of the problem.

**Superseded in part.** Findings 1 and 2 assumed a short board and
asymmetric action tiles (raise one stat, lower another by less). Action tiles
are now symmetric hidden ±X on a long board
([doc 03](03-board-and-tiles.md#action-tiles)). Reachability is a landing-count
problem; the negative path does not need sacrifice tiles. Findings 3–7
(scoring leak, marriage, children, education) still apply.

---

## Finding 1 — The top perk tiers are unreachable

With tiers at ±25/50/75/100 and the originally proposed ±3 to ±8 stat deltas, a
full run contains 13 action tiles and ~3 stat-moving life events. That gives a
realistic ceiling of about **87 points** in your best stat — so **±100 is
unreachable and ±75 is marginal.** Two of the four tiers per direction would be
dead content.

| Action delta | Best case | Realistic peak | Top tier reached |
| --- | --- | --- | --- |
| ±3 … ±8 | 164 | 87 | ±75 |
| **±5 … ±15** | 255 | 122 | **±100** |
| ±8 … ±20 | 320 | 152 | ±100 |

**Fix applied:** action tile deltas move to **±5 to ±15**, life events to
**±10 to ±20**. This is the smallest change that makes all four tiers reachable
while still requiring sustained commitment — a maxed stat takes most of the board
pushing one direction.

## Finding 2 — The negative path can't get deep

This one is structural and easy to miss. The tile authoring rule says each option
raises one stat and lowers another by a *smaller* amount (+5/−3). That means
**stats move down more slowly than they move up**, so a player committed to the
negative path simply can't reach the deep tiers:

| Sacrifice tiles | Negative tiers held | Peak stat | Depth vs. positive build |
| --- | --- | --- | --- |
| *(positive build)* | 4.0 | 88 | — |
| 0 | 1.7 | 64 | **43%** |
| 2 | 2.4 | 72 | 61% |
| **4** | 3.1 | 85 | **78%** |
| 6 | 3.7 | 95 | 92% |

At 43% depth the central gamble of the game isn't a gamble — the negative path is
mechanically locked out of its own payoff.

**Fix applied:** roughly **4 of the 13 action tiles offer a "sacrifice" option** —
drop one stat by the full delta and take cash. Thematically this is the
sell-your-soul choice (take the bribe, ditch the friend, skip the surgery), and
it's the negative path's on-ramp. It also hands negative builds their in-run cash
through a player decision rather than a passive perk, which reads better.

## Finding 3 — Positive multipliers leak to negative builds

The most important finding, and the reason the balance couldn't be tuned by
turning one dial.

Because every action option moves one stat up and another down, a committed
negative build **accidentally accumulates positive tiers in its off-stats** —
about 1.3 of them. Under a scoring rule that counts every positive tier held,
those tiers earn multipliers the player never committed to. So raising the
positive multiplier to help positive builds **also buffs negative builds**, and
the gap never closes:

| Scoring | Positive mult | Positive score | Negative score | Gap |
| --- | --- | --- | --- | --- |
| Gross (count all positive tiers) | 10% | $1,131k | $1,808k | −37% |
| Gross | 30% | $1,780k | $2,229k | −20% |
| Gross | 50% | $2,430k | $2,650k | **−8%** |
| Net (negative tiers cancel positive) | 10% | $1,073k | $1,597k | −33% |
| Net | 30% | $1,607k | $1,597k | **+1%** |
| Net | 50% | $2,140k | $1,597k | +34% |

Under gross scoring the dial barely responds — you'd need a 50%+ per-tier
multiplier just to approach parity, and you'd still be chasing. Under net scoring
the dial behaves normally and parity lands at a sane value.

**Fix applied — score on net tiers:**

```
scoring tiers = max(0, positive tiers held − negative tiers held)
final score   = net worth × (1 + scoring tiers × multiplier) + bonuses
```

Beyond fixing the math, this is better design: it means **the end-game bonus
rewards actual commitment**, not incidental drift. You can't hedge your way into
a multiplier.

## Finding 4 — Parity, and the two dials

With Findings 1–3 applied, the two dials can be solved against each other. Each
negative tier pays cash per payday; each net positive tier multiplies final net
worth:

| Negative perk value (per payday, per tier) | Required positive multiplier per tier |
| --- | --- |
| $6k | 15.6% |
| $12k | 23.3% |
| **$18k** | **29.6%** |
| $24k | 35.5% |
| $30k | 40.7% |

**Recommended starting point: negative perks worth ~$18k per payday per tier,
positive perks worth ~30% of net worth per net tier.** At those values a
committed positive build holds 4.0 tiers (≈ +120% on net worth) and a committed
negative build holds 3.1 tiers (≈ $670k extra cash over a run).

### Resulting archetype spread

| Archetype | Mean score | Std dev | p10 | p90 |
| --- | --- | --- | --- | --- |
| Committed positive | $1,597k | $520k | $981k | $2,271k |
| Committed negative | $1,597k | $408k | $1,107k | $2,139k |
| Uncommitted / drifting | $975k | $362k | $562k | $1,441k |

Means are level — the parity target from
[doc 02](02-character-and-stats.md#the-intended-risk-curve) is met. Two problems
remain:

**The variance is backwards.** The negative build should be the *high*-variance
option, but it comes out lower ($408k vs. $520k) because its payoff is modelled
as steady per-payday cash, which is the most reliable income in the game. If the
negative path is meant to feel like a gamble, **negative perks should be swingy
rather than salaried** — one-off windfalls, double-or-nothing effects, risky
bonuses — not a stipend. This is a content directive for perk authoring, not a
number to tune.

**Uncommitted play is punished hard** — 39% behind both committed builds. The
intent was "slightly below." Worth deciding whether that's acceptable (it
strongly teaches commitment) or whether the multiplier should be flattened with a
larger base and smaller per-tier step. See
[Q2 in doc 08](08-open-questions.md#q2--how-harshly-should-uncommitted-play-be-punished).

## Finding 5 — Education pays, by about the right amount

| Path | Paydays | Mean score | Net worth | vs. no school |
| --- | --- | --- | --- | --- |
| No school (tier 1) | 12 | $1,385k | $698k | — |
| Undergrad (tier 2) | 11 | $1,597k | $787k | +15.4% |
| Grad (tier 3) | 10 | $1,753k | $839k | +26.6% |

This matches the ~28% target from
[doc 05](05-economy-and-investments.md#salary-bands). Grad school is clearly
better but not mandatory, and the no-school player's advantage — debt-free with
two extra paydays — is real. **No change recommended**; the salary bands as
written work.

## Finding 6 — Marriage: the original spec was right, my proposal was wrong

This reverses the concern raised in [doc 04](04-life-events.md#marriage).

| Cost scoping | Married score | vs. single | Loans taken |
| --- | --- | --- | --- |
| Single baseline | $1,597k | — | $116k |
| **All costs double (spec as written)** | $1,529k | **−4.3%** | $396k |
| Involuntary costs only (my proposal) | $1,949k | **+22.0%** | $234k |

The spec as written lands at −4.3% — close enough to neutral that marriage is a
genuine judgement call rather than an obvious yes or no. The "fix" of limiting
the doubling to involuntary costs makes marriage **+22%, an automatic take**,
which is a worse outcome than the problem it was meant to solve.

So: **keep the original rule — 50% of a spouse's salary, and any cost incurred is
doubled.** The intuition that it looked like a trap was wrong, because it
undercounted how much a spouse's salary compounds once it's flowing into the
investment account.

The loan figure is the other story here: married players borrow **$396k vs.
$116k**, more than triple. That's the liquidity system working exactly as
intended — doubled costs mean a bigger cash buffer is needed, and a married
player who over-invests gets squeezed into loans, which drains karma and makes
their mid-life crisis worse. Marriage isn't a money decision so much as a
*liquidity* decision.

## Finding 7 — Children need to be worth about $150k each

Children currently cost money and return only score, so they need a score value
large enough to make the choice real:

| Score per child | Single, 2 kids | Married, 2 kids | vs. childless |
| --- | --- | --- | --- |
| $0 | $1,287k | $1,316k | −19.4% |
| $60k *(first guess)* | $1,407k | $1,436k | −11.9% |
| $120k | $1,527k | $1,556k | −4.4% |
| **~$150k** | — | — | **≈ 0%** |
| $180k | $1,647k | $1,676k | +3.1% |

**Recommended: ~$150k per child**, about 2.5x the original guess. Below ~$120k
declining is always correct and both child events become non-decisions.

Note that a married player pays double for children, so no single value balances
both cases perfectly. Leaving children slightly *negative* in pure score terms is
defensible if they also unlock spring-season content, which would carry the rest
of the value — see [Q3 in doc 08](08-open-questions.md#q3--what-else-do-children-unlock).

## Finding 8 — What happens if stats are added back?

The system is three stats today, reworked down from an earlier five, and may grow
again. Re-solving parity at each stat count:

| Stats | Positive tiers held | Peak stat | Parity multiplier | vs. 3 stats |
| --- | --- | --- | --- | --- |
| **3** | 4.0 | 88 | **29.5%** | — |
| 4 | 3.8 | 83 | 34.2% | +16% |
| 5 | 3.5 | 78 | 38.4% | +30% |

**The tuning is robust to adding stats.** A committed build focuses the same two
stats no matter how many exist, so tier depth barely moves. Extra stats mostly
add off-stat drift, which net-tier scoring already discounts. Adding a stat means
re-solving one number — the positive multiplier rises about 30% going from three
stats to five — and nothing structural.

The two real costs are elsewhere:

- **Content scales linearly:** 8 more perks per stat, plus action tile options
  that move it.
- **Depth dilutes:** peak reachable stat falls from 88 to 78, which pushes the
  ±100 tier back toward unreachable and re-triggers
  [Finding 1](#finding-1--the-top-perk-tiers-are-unreachable). Five stats would
  need larger deltas or more action tiles.

**Implication:** build the stat system data-driven — stats as a list, perk
effects as data — so a fourth stat is content work plus one retune, not a
refactor.

---

## Summary of changes to the design

| Finding | Change |
| --- | --- |
| 1 | Action tile deltas ±5…±15, life events ±10…±20 |
| 2 | ~4 action tiles offer a sacrifice option (full stat drop for cash) |
| 3 | Score on **net** tiers — negative tiers cancel positive ones |
| 4 | Negative perks ≈ $18k/payday/tier; positive ≈ 30% per net tier |
| 4 | Negative perks should be **swingy**, not a steady stipend |
| 5 | Salary bands unchanged |
| 6 | **Keep the original marriage rule** — all costs double |
| 7 | ~$150k final score per child |
| 8 | Stat count is safe to change later; keep the system data-driven |

## What this model does not cover

- Perk *content* — it models perks as abstract cash and multipliers, so it can
  tell you the budget but not whether the perks are interesting.
- Player skill, misplays, and learning curve.
- Investment policy beyond a fixed cash buffer. A sharper player would vary
  the buffer by what's coming up on the board, which the camera lets them see.
- Any interaction between players, since there is currently none.
- Turn order and board position effects — everything is modelled per payday.
- Wall-clock pacing of asynchronous multiplayer, which is modelled separately in
  [`tools/async_pacing.py`](../tools/async_pacing.py) and written up in
  [doc 06](06-modes-and-multiplayer.md#pacing-and-session-length).
