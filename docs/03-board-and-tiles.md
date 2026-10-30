# 03 — Board & Tiles

## Structure

**Spec.** A defined path every player travels, with minor deviations driven by
life events. Three main tile types: salary, action, and outcome. Tile content
correlates to how far along the board you are, so later tiles are thematically
later-in-life.

## Tile types

### Salary tiles
**Spec.** Spaced throughout the board. Players who **land on or move past** them
collect their salary.

Because passing counts, salary income is fully predictable — everyone banks every
payday. That's deliberate: it makes income a planning baseline rather than a
luck roll, and it's the hook the promotion/layoff system hangs on (see
[doc 04](04-life-events.md#promotions-and-layoffs)).

### Action tiles
**Settled.** Each action tile is a life choice with two options. One option
raises a stat by a fixed amount **X**; the other lowers either the same stat or a
different stat by the same **X**. The expected value of a random pick is zero —
there is no natural drift upward.

**The player does not see which stat moves, or in which direction, until after
they choose.** They pick on the flavor of the action, not on a spreadsheet.
Over a long game that becomes a lifestyle: consistently "good" choices drift
every stat up; consistently "bad" choices drift every stat down; mixing stays
near zero.

Thematic rule: **virtuous / effortful / generous actions raise a stat; lazy /
selfish / short-sighted actions lower one.** Example:

> *Train for a half marathon — pay $100.* → Brawn **+10** (revealed after)
> *Snack time on the couch.* → Brawn **−10** (revealed after)

**Authoring rules.**

- Both options move the same magnitude X. Default X is **10**, so ten committed
  hits max a stat. Varying X per tile is allowed later; don't mix magnitudes
  inside one tile.
- Option A is the "good" action and always **+X**. Option B is the "bad" action
  and always **−X**. Never invert this — players should be able to learn the
  pattern from flavor even though the numbers are hidden.
- The two options may hit the **same** stat (the marathon example) or **two
  different** stats (study late vs. go to the party: Brains +10 vs. Buds −10).
  Same-stat tiles are the on-ramp for a committed path; split-stat tiles are
  the interesting ones.
- Money is a secondary rider, and it should usually **oppose** the stat: the
  good option costs money or time, the bad option is free or pays. That is how
  the negative path earns cash without a stipend perk — skipping the marathon
  keeps the $100.
- One sentence per option. No third choice. No "obviously correct" answer once
  money is on the table.

This spec supersedes the earlier two-stat-offset proposal (raise one, lower
another by a smaller amount). That version created upward drift and made the
negative path mechanically harder to walk. Symmetric hidden ±X does not.

### Outcome tiles
**Spec.** Look like normal tiles from the classic game. Preset result, no choice:
gain money, lose money, gain karma, lose karma.

These are the pacing relief between decisions, and the randomness that keeps two
players making identical choices from finishing identically.

### Life event tiles
**Proposal.** The major forks ([doc 04](04-life-events.md)) are **mandatory
stops** — you halt on them regardless of your roll, as "stop" spaces work in the
original. Without this, a bad roll could skip your wedding or your mid-life
crisis, and the structural beats of the game would be luck-dependent.

## Board length and movement

**Spec intent.** The board is long — lots of life tiles — so a player who
commits can actually max a skill tree. 72 tiles was a placeholder from an
earlier pacing pass and is **too short** for that. Exact length is still open;
the constraint is not "how short can we go" but "how many decisions does a
committed player resolve before retirement."

With X = 10 and three stats, a fully committed "always good" player spreads
gains across whatever stats the tiles happen to touch:

| Action tiles landed | Expected per stat | Top tier reached |
| --- | --- | --- |
| 15 | +50 | ±50 |
| 24 | +80 | ±75 |
| **30** | **+100** | **±100 on all three, if capped** |
| 40 | +133 (capped) | ±100, with room to recover from mixes |

So the design target is **roughly 30+ action-tile landings per run**, plus
outcome tiles, salary tiles, and mandatory life events. That is a much bigger
board than 72, *or* a different rule for how often tiles resolve.

**The landing problem.** A 1–6 spinner averages 3.5 spaces, so you only *land
on* about 30% of tiles. Doubling the board does not double the decisions unless
movement shrinks too. Three ways to hit 30 action landings:

| Approach | What it does | Cost |
| --- | --- | --- |
| **A. Long board, smaller spinner (1–3)** | More landings per tile of board | More turns → longer async games |
| **B. Action tiles are stop spaces** | You resolve every action tile you reach, like life events | Every action is mandatory; board can stay shorter |
| **C. Pass-and-resolve for action tiles** | Landing *or passing* an action tile triggers it | Dense, fast, easy to overshoot the decision budget |

This is the real board-length question now. See
[Q4 in doc 08](08-open-questions.md#q4--how-do-we-get-enough-action-landings).

Salary tiles still pay on pass. Life events are still mandatory stops.

## Seasons

**Spec.** Scenery transitions through the game: summer → fall → winter → spring,
ending in spring with retirement.

**Proposal — four equal quarters** of whatever the final board length is, each
with its own content theme:

| Season | Life stage | Tile content themes |
| --- | --- | --- |
| Summer | Youth, first job | School, first apartment, first car, friendships, bad habits |
| Fall | Building | Career push, marriage, mortgage, moving, falling out of touch |
| Winter | Midlife | Kids, aging parents, burnout, mid-life crisis, health |
| Spring | Late career, retirement | Legacy, reconciliation, grandkids, letting go, retirement |

Ending on spring reads as rebirth rather than decline, which sets the tone for
retirement being a payoff rather than an ending.

## Content as season decks

**Proposal.** Each board position gets a fixed **type** (action/outcome) and
**season tag**. The actual text is drawn from that season's deck when the game
starts (and, for gated cards, filtered by married / parent / education flags).

This keeps content matching life stage, makes two games on the same board feel
different, and makes expansion additive: new cards go into a season deck without
touching layout.

Working authoring budget, sized for a long board with ~30 action landings and
a 2× deck so repeats stay rare:

| | Per season | Total |
| --- | --- | --- |
| Action cards | ~40 | **~160** |
| Outcome cards | ~25 | **~100** |

Each action card is 2 options, so ~320 authored choice lines. That is the
largest content job in the project. Lists live in
[docs/content/](content/README.md).

## Deviations from the main path

The concept mentions minor deviations off the main path. The ones identified so
far are the **university track** and the **grad school extension**
([doc 04](04-life-events.md#university)) — short side loops that cost tiles and
money and rejoin the main path.

Open: whether any mid-game or late-game branches exist, or whether the path is
single after the education fork. See
[Q8 in doc 08](08-open-questions.md#q8--are-there-branches-after-university).
