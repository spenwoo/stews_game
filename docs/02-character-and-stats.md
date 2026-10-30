# 02 — Character & Stats

## Character creation

**Spec.** Games open on a character design screen. The player picks from a set of
appearance features, then assigns starting skill points.

Appearance options:

| Feature | Choices |
| --- | --- |
| Body | Male / female |
| Hair | Style, color |
| Shirt | Style, color |
| Pants | Style, color |

**Proposal — option counts.** 6 hair styles, 8 hair colors, 5 shirt styles,
8 shirt colors, 4 pants styles, 8 pants colors, per body type. Enough for every
player in a 6-player lobby to look distinct at a glance, which matters because
you identify opponents by silhouette on the board. All cosmetic, zero mechanical
effect.

## The stat system

**Spec.** Three stats, each running from −100 to +100, moved by the choices you
make on action tiles. Crossing thresholds unlocks perks. **Karma is tracked
separately** as its own resource, outside the perk system.

The system was originally five skills and was deliberately reworked down to
three. It may grow again later — see [below](#if-stats-are-added-back).

| Stat | Is | Tagline |
| --- | --- | --- |
| **Brains** | Intellect | "Intellectual superiority" |
| **Brawn** | Physical toughness | "How tough are ya" |
| **Buds** | Friendship, social pull | "Friendship is my power" |

(The one-liners are stated the right way round here; they were crossed in the
original write-up.) *Charisma* as referenced in the layoff formula maps onto
Buds; *intellect* onto Brains.

Perk count: 3 stats × 8 thresholds = **24 perks** to author.

### If stats are added back

Since the count may change, it's worth knowing what a fourth or fifth stat would
cost. Modelled in
[doc 09, Finding 8](09-balance-model.md#finding-8--what-happens-if-stats-are-added-back):

| Stats | Peak stat reached | Parity multiplier | Perks to author |
| --- | --- | --- | --- |
| 3 | 88 | 29.5% | 24 |
| 4 | 83 | 34.2% | 32 |
| 5 | 78 | 38.4% | 40 |

**The balance survives it.** A committed build focuses the same two stats
regardless of how many exist, so tier depth barely moves; extra stats mostly add
off-stat drift, which net-tier scoring already discounts. Adding a stat means
re-solving the positive multiplier (up ~30% at five stats) and nothing more
structural.

Two real costs, though:

- **Content scales linearly.** Each stat is 8 more perks, plus action tile
  options that move it.
- **Depth dilutes.** Extra stats spread the same landings thinner, so ±100
  needs even more action tiles (or a longer board) to stay reachable.

**Implication for later:** build the stat system data-driven, with stats as a
list rather than three named fields, and keep perk effects as data. Then adding a
stat is content work plus one number, not a refactor.

### Karma

Karma is a separate resource, not a stat. It has no perk tiers. Its jobs are:

- Gained and lost on outcome tiles.
- Reduced by taking bank loans ([doc 05](05-economy-and-investments.md#loans)).
- Gained by adopting children ([doc 04](04-life-events.md#children)).
- **The input to the mid-life crisis resolution**
  ([doc 04](04-life-events.md#mid-life-crisis)) — its single most important use.
- A contributor to final score.

Because karma sits outside the perk system, it needs its own range and its own
reason to be managed turn to turn. See
[Q1 in doc 08](08-open-questions.md#q1--how-does-karma-work-as-a-separate-resource).

### Unresolved: do stats start at zero?

The concept says both that players assign skill points during creation and that
every stat starts at zero. Those can't both hold.

**Proposal.** Stats start at zero and the creation screen gives you a small
budget — **10 points, max +4 into any single stat** — to spend. You begin
slightly specialized rather than blank, the starting spread stays narrow enough
that it doesn't decide the game, and "starts at zero" stays true as the baseline.
See [Q5 in doc 08](08-open-questions.md#q5--starting-skill-points).

## Perk tiers

**Spec.** As stats rise and fall, players unlock levels with perks. Negative
perks are more powerful; positive perks unlock bonuses at the end of the game.
Choosing a path is a gamble.

**Proposal — threshold layout.** Tiers at ±25, ±50, ±75, ±100, giving four
positive and four negative tiers per stat — **24 perks total**. Perks are
cumulative while you hold the threshold, and are **lost if your stat drops back
below it** — so a negative build can be walked back, at the cost of the turns it
takes to do it.

Reachability is a board-length problem, not a delta problem. Action tiles move a
stat by a fixed **X (default 10)**, hidden until after the choice
([doc 03](03-board-and-tiles.md#action-tiles)). Ten committed hits max a stat.
The board is intended to be long enough that a player who consistently picks
one direction can fill the tree — see
[doc 03, Board length](03-board-and-tiles.md#board-length-and-movement).

### The intended risk curve

| Path | When it pays | What it gives |
| --- | --- | --- |
| Positive | End of game | Score multipliers and bonuses |
| Negative | Immediately | In-run power: more cash, cheaper costs, board control |

**Target:** a committed negative build and a committed positive build should land
within ~10% of each other in final score, with the negative build carrying higher
variance. Uncommitted builds should land slightly below both — commitment is what
the system rewards.

**Status: the on-ramp problem is gone.** The earlier model assumed each option
raised one stat and lowered another by *less*, which made going negative harder
than going positive. The actual spec is symmetric hidden ±X, with "good" = up
and "bad" = down. A committed couch-potato reaches −100 as easily as a committed
marathoner reaches +100. [Doc 09, Finding 2](09-balance-model.md) is superseded.

The remaining balance job is still the two dials — how much negative perks pay
*during* the run vs. how much positive perks multiply at the end — plus the
fact that **bad options should often be the cheaper ones**. That gives the
negative path its in-run cash through the tiles themselves, so negative perks
can be swingy extras rather than a salary.

Uncommitted play (mixing good and bad) stays near zero and collects neither
deep negative cash nor a big end multiplier. How harsh that should feel is
still [Q2](08-open-questions.md#q2--how-harshly-should-uncommitted-play-be-punished).

### Perk design rules

So the perks stay writable and legible:

- A perk is one sentence, with one effect, no sub-conditions.
- Positive perks never pay out mid-game; negative perks never pay out at the end.
- Negative perks should be **swingy** — windfalls, gambles, double-or-nothing —
  rather than steady income. A lot of the negative path's cash should already
  come from skipping costly "good" actions on the tiles themselves.
- No perk may permanently remove another player's agency (multiplayer stays
  friendly).
- Action tiles move stats by a fixed **X, default 10**. Life events may move
  more (±10 to ±20) because there are few of them.
