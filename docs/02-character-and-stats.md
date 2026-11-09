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

**Settled.** Karma is a separate **currency**, not a stat and not a 0–100
meter. No cap. Hidden from other players. It moves whenever a tile or event
says so (loans, adoption, outcomes, riders), flavors the mid-life crisis, and
adds an uncapped line at retirement so two similar-looking lives can finish
far apart. Details:
[doc 12](12-karma-health-housing-start.md#1-karma).

### Opening class (natures)

**Settled direction.** The old "spend 10 points at creation" idea is replaced.
Pick one **class**: +15 in one stat, −15 in another, or **Ambivalent** (all zero).
Seven total. Youth tiles then move those numbers before the University STOP,
so the opening bias is a start, not a prison.

Full table, names, and the Brawn/Buds early-game doors (scholarship, legacy
letter) so Brains isn't the only reason to exist:
[doc 12](12-karma-health-housing-start.md#5-opening-class--nature).

## Perk tiers

**Spec.** As stats rise and fall, players unlock levels with perks. Negative
perks lean in-run and swingy; positive perks mix retirement bonuses with
in-run effects (the Excel list is the source). Choosing a path is a gamble.

**Settled — threshold layout.** Tiers at ±25, ±50, ±75, ±100. At each
threshold the player **picks one of two perks**. Earlier picks never gate
later ones. 3 stats × 2 directions × 4 tiers × 2 choices = **48 perks
authored**; a fully committed stat-direction holds **4** of them.

**You only have a perk while you currently hold that level.** Crossing +50
unlocks a pick; if the stat falls to +40 that perk turns off until you climb
back. The *choice* is remembered — you do not re-pick. Same rule on the
negative side. Worked example and the full list:
[content/perks.md](content/perks.md).

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
- At each threshold, two options of similar power and different shape. The
  player picks one; that pick never restricts a later threshold.
- **Active only while the stat currently meets that threshold.** Drop below
  it and the perk goes dormant, even if you already unlocked it.
- Timing is per-perk on the sheet — positives are no longer "retirement only."
  See [content/perks.md](content/perks.md).
- Negative perks should be **swingy** — windfalls, gambles, double-or-nothing —
  rather than steady income. A lot of the negative path's cash should already
  come from skipping costly "good" actions on the tiles themselves.
- **Bully** (Brawn −25) takes **$500** from a player within 10 tiles whenever
  they are paid. Early on purpose, so it can tick for most of the run.
- Action tiles move stats by a fixed **X, default 10**. Life events may move
  more (±10 to ±20) because there are few of them.
