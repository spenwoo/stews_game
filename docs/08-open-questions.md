# 08 — Open Questions

What's still undecided, ordered by how much other work it blocks. **Blocking**
means content authoring can't proceed correctly until it's answered.

Questions resolved so far are listed at the bottom, with where the answer lives.

---

## Q1 — How does karma work as a separate resource?

**Blocking.** Karma is now a standalone resource rather than a stat with perk
tiers ([doc 02](02-character-and-stats.md#karma)), which leaves its design
underspecified. It needs:

- **A range.** Does karma run −100 to +100 like the stats, or is it unbounded?
  Can it go negative at all?
- **A starting value.** Zero, or a small positive float?
- **Enough sources to be managed.** Right now its inputs are outcome tiles, loans
  (−5 each), and adoption (+15). In the model, every archetype finished at
  roughly −10 karma, driven mostly by loans — so karma currently behaves as a
  borrowing counter rather than a resource players steer. It needs action-tile
  sources too, or it'll feel like a penalty meter.
- **A score value.** The formula currently assumes $2k per point
  ([doc 05](05-economy-and-investments.md#final-scoring)). Is karma meant to score
  at all, or is its only job the mid-life crisis roll?

The mid-life crisis is the one place karma decisively matters
([doc 04](04-life-events.md#mid-life-crisis)). If that stays its only real use,
karma is effectively a single-use resource saved up across 50 tiles for one roll
— which is defensible and dramatic, but should be a deliberate choice rather than
a side effect.

## Q2 — How harshly should uncommitted play be punished?

**Blocking (affects the multiplier shape).** At the tuned numbers, an
uncommitted player scores **39% below** either committed build
([doc 09, Finding 4](09-balance-model.md#resulting-archetype-spread)). The stated
intent was "slightly below."

| Option | Effect |
| --- | --- |
| **A. Accept it** | Commitment is the game's central lesson; a 39% penalty teaches it hard and fast |
| B. Flatten the curve | Larger base multiplier, smaller per-tier step — softer landing for hedgers, less dramatic payoff for committers |
| C. Add a mid-tier reward | Something for ±25/±50 that doesn't require going deep, so partial commitment pays partially |

Worth deciding from feel: is a first-time player who makes reasonable-seeming
choices supposed to lose badly, or come close?

## Q3 — What else do children unlock?

**Settled.** Mix is in [content/family.md](content/family.md): payday upkeep
($4k/child, doubled if married), parent-only tiles, optional college-for-kid
stop, karma/Buds-weighted legacy bonus, `no_children` spring slice. Second
stop can still decline. Numbers are starting points.

## Q4 — How do we get enough action landings?

The board is meant to be **long**, so a committed player can max a skill tree.
With X = 10 and three stats, that wants **~30 action-tile resolutions** per run
([doc 03](03-board-and-tiles.md#board-length-and-movement)). 72 tiles with a 1–6
spinner only lands you on ~21 tiles total — not enough.

The open question is the *mechanism*, not the ambition:

| Option | Hits 30 actions by… | Async cost |
| --- | --- | --- |
| A. Long board, spinner 1–3 | More turns, more landings | Solo longer; 6-player games stretch |
| B. Action tiles are stop spaces | Every action on the path resolves | Fewer tiles needed; every action is mandatory |
| C. Pass-and-resolve on action tiles | Passing counts, like salary | Dense; easy to overshoot |

B is the closest to the original Game of Life's "STOP" spaces and keeps the
turn count from exploding. A is the most literal "lots of tiles." Worth a
deliberate pick before the action-tile list is sized, because the authoring
budget follows from it.

Lobby size still changes async duration more than board length does — show an
estimated duration at lobby creation regardless.

## Q4b — Is pipelined turn order acceptable?

Strict sequential turns were chosen for a live session, where they cost nothing.
Asynchronously they cost **24.7 days** for a 6-player game, versus 8.5 days
pipelined ([doc 06](06-modes-and-multiplayer.md#pipelined-turn-order)).

The proposal keeps turn order intact — you never move ahead of the player in
front of you on the same round — but lets a responsive player take their next
turn without waiting for everyone behind them. Worth confirming this still
matches the intent of "each player taking turns," since it means two players can
be thinking at the same time.

## Q5 — Starting skill points

The concept says players assign skill points at creation *and* that stats start
at zero. Pick one:

- **A.** Small budget at creation — proposal: 10 points, max +4 per stat.
- **B.** All stats start at zero; the creation screen is purely cosmetic.

Low stakes either way (the model shows starting points barely move final score
against ±100 ranges), but it changes whether the creation screen has a strategic
layer.

## Q5b — Will more stats be added?

The system was reworked from five stats down to three, and may grow again. Not
blocking — [doc 09, Finding 8](09-balance-model.md#finding-8--what-happens-if-stats-are-added-back)
shows the balance survives it, needing only a retune of the positive multiplier
(+30% going from three stats to five).

What it does affect is **when to commit**:

- Perk content scales linearly, 8 per stat. Authoring 24 perks and later wanting
  40 means revisiting all of them for consistency, so it's cheaper to decide
  before perk authoring starts than after.
- At five stats, peak reachable stat falls to 78 and the ±100 tier goes back out
  of reach, so stat count and delta sizes have to be set together.
- The implementation should treat stats as a list and perks as data regardless,
  so the door stays open cheaply.

If there are candidate fourth and fifth stats in mind, now is the cheap moment to
name them even if the decision comes later.

## Q6 — Career list and career perks

Content question, not blocking, but the largest single job after tile content:

- How many careers per tier? (Proposal: 6 / 6 / 5.)
- Which tier-3 careers are "enhanced versions" of tier-2 careers, as the concept
  describes, versus wholly separate?
- What non-money perk does each career get at Senior and Executive? Without
  these, careers are interchangeable salary numbers wearing job titles.

## Q7 — How punishing should a layoff be?

A layoff at payday 9 drops an Executive to a base-tier job, which is close to
run-ending. Candidate softeners
([doc 04](04-life-events.md#promotions-and-layoffs)):

- Severance worth ~2 paydays.
- Reroll respects your education tier.
- Payday counter resets to 2, not 0.
- Executive stage is layoff-immune.

Note that layoff risk already does useful work in the current balance: negative
builds have low Brains and Buds, so they sit near the 12% ceiling and get laid
off often. That's a meaningful counterweight to their cash advantage, so
softening layoffs will shift the parity numbers in
[doc 09](09-balance-model.md#finding-4--parity-and-the-two-dials).

## Q8 — Are there branches after university?

The concept mentions "minor deviations based on life events," and university plus
grad school are the only ones identified. Is the path single after that, or are
there later short branches (career-change loop, divorce detour, early retirement
shortcut)?

Branches are cheap thematically but expensive for balance, since players on
different-length paths hit different numbers of paydays — which the model shows
is the dominant variable in lifetime earnings.

## Q9 — What information is public?

**Settled.** Lives sheet is openable at any time. Public: age/position, job,
house name, married, children. Hidden until retirement: cash, salary,
investments, karma, exact stats. See
[doc 06](06-modes-and-multiplayer.md#the-shared-hud).

Still open: do **perk names** show (you can infer the path) or only life-status
fields? Proposal: hide perks too — otherwise a "Well-Connected" tag tells
everyone you went deep positive Buds.

## Q10 — Should proximity enable interaction?

The 10-tile visibility rule is currently cosmetic, and **Buds — a whole stat
about friendship — has no inter-player expression at all.** In the current model
Buds is purely layoff insurance, which is a thin job for a stat whose tagline is
"friendship is my power."

Worth considering proximity-gated interactions: gifts, favors, small Buds gains
for travelling near others, cooperative options on some action tiles.

Counter-argument: it adds multiplayer-only mechanics, breaking the "solo and
multiplayer are functionally identical" goal in
[doc 06](06-modes-and-multiplayer.md#the-two-modes).

---

## Smaller undecided items

- Spinner vs. dice; whether any perk modifies movement.
- Can a player decline to buy a house? Buy more than one? Upgrade later?
- Does the game end when the first player retires, or does everyone finish?
  (Proposal: everyone finishes.)
- Is the investment deposit instant while withdrawal is delayed? (Proposal: yes —
  the asymmetry is what creates the liquidity trap.)
- Partial investment withdrawals allowed? (Proposal: yes.)
- Is there a board-overview camera, or only the road view?
- How far ahead down the road are upcoming tiles legible? This is a real
  information decision — it determines whether investment liquidity is a read or
  a guess.
- Lobby/invite flow: joinable by code or link.
- Can a player join after a game has started? (Almost certainly not.)
- What happens if a player quits outright — auto-play to the end, or drop from
  standings?
- Can one player run several games at once? (Likely yes, and probably necessary
  for a multi-day cadence to feel sustainable.)
- Is there a "nudge a slow player" action, and can it be abused?
- Does the recap replay other players' turns in 3D, or summarize them as cards?

### Async-specific traps worth avoiding

Noting these now because they're cheap to design around and expensive to retrofit:

- **Never tie anything to wall-clock time.** Investment returns resolve per
  payday, not per day. If returns accrued in real time, players would learn to
  sit on their turn, and a slow player would out-earn an attentive one.
- **Auto-played turns must take the least destructive default** — first option,
  decline optional events, no investment change — so the backstop never loses a
  game for someone.
- **Notifications are the whole delivery mechanism**, so per-move notifications
  for other players are the fastest route to being muted. Other players' moves
  belong in the recap.

---

## Resolved

| Question | Answer | Where |
| --- | --- | --- |
| Three stats or five? | Three — Brains, Brawn, Buds, reworked down from five. Karma is a separate resource. May grow again (Q5b) | [doc 02](02-character-and-stats.md#the-stat-system) |
| Brains vs. Brawn meaning | Brains = intellect, Brawn = toughness (the original taglines were swapped) | [doc 02](02-character-and-stats.md#the-stat-system) |
| Session structure | Solo is one ~10 min sitting; multiplayer is **async over days** with push notifications and no shot clock | [doc 06](06-modes-and-multiplayer.md#the-two-modes) |
| Simultaneous turns? | No — players take turns in order, pipelined so fast players aren't blocked (Q4b) | [doc 06](06-modes-and-multiplayer.md#pipelined-turn-order) |
| Any time limit at all? | A 24h auto-play backstop so games terminate; fires on ~4% of turns | [doc 06](06-modes-and-multiplayer.md#timeouts) |
| Are the top perk tiers reachable? | Yes, by making the board long enough (~30 action landings at X=10). Mechanism still Q4 | [doc 03](03-board-and-tiles.md#board-length-and-movement) |
| Can a negative build get deep? | Yes — action tiles are symmetric hidden ±X, good = up, bad = down. No sacrifice tiles | [doc 03](03-board-and-tiles.md#action-tiles) |
| What do other players see? | Lives sheet: position, job, house, family. Hide money, salary, karma, stats | [doc 06](06-modes-and-multiplayer.md#the-shared-hud) |
| How do negative perks convert to score? | They don't. Scoring is on **net** tiers | [doc 09 F3](09-balance-model.md#finding-3--positive-multipliers-leak-to-negative-builds) |
| What are the perk dials? | ~$18k/payday/tier negative, ~30% per net positive tier | [doc 09 F4](09-balance-model.md#finding-4--parity-and-the-two-dials) |
| Does education pay for itself? | Yes, ~27% spread. Bands unchanged | [doc 09 F5](09-balance-model.md#finding-5--education-pays-by-about-the-right-amount) |
| Is marriage worth it? | Yes — and the original rule (all costs double) was right | [doc 09 F6](09-balance-model.md#finding-6--marriage-the-original-spec-was-right-my-proposal-was-wrong) |
| What are children for? | Upkeep + parent tiles + college stop + legacy bonus; `no_children` gets a different spring | [content/family.md](content/family.md) |
| Divorce? | Yes — payday check scaled by Buds, plus a mid-life crisis face | [doc 04](04-life-events.md#divorce-and-buds) |
| Spouse promote / layoff? | Promotes with you. Cannot be laid off | [doc 04](04-life-events.md#marriage) |
