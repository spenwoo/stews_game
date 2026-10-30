# 06 — Modes & Multiplayer

## The two modes

**Spec.** Two modes, solo and multiplayer. Gameplay is functionally the same in
both. Solo is faster to play and focused on reaching a high score. Multiplayer
supports up to 6 players, each taking turns.

**Spec — the cadences are different, not just the speed.**

| | Solo | Multiplayer |
| --- | --- | --- |
| Session | One sitting, ~10 min | **Asynchronous over days** |
| Turn prompt | Immediate | Push notification |
| Time pressure | None | None, or very generous |
| Goal | High score | Standings against 2–6 players |

Identical rules, identical board, identical scoring. One rules engine, one
content set, one balance pass. Solo adds a persistent high-score table;
multiplayer adds final standings.

Asynchronous play is a significant constraint on everything downstream, because
it means **game state lives on a server, not a device**, and a game may be
mid-flight for two weeks.

## Pacing and session length

Solo is straightforward. Using the 72-tile board from
[doc 03](03-board-and-tiles.md#board-length-and-movement), a run is ~13 action
tiles, ~8 outcome tiles, and 6 life events:

| Turn type | Count | Est. time | Subtotal |
| --- | --- | --- | --- |
| Action tile (read, choose) | 13 | 20s | 4m 20s |
| Outcome tile (read, tap) | 8 | 8s | 1m 4s |
| Life event (bigger decision) | 6 | 45s | 4m 30s |
| | | **Per player** | **~10 min** |

Multiplayer is where it gets interesting, and the answer is not intuitive.
Modelled in [`tools/async_pacing.py`](../tools/async_pacing.py) against a
realistic response pattern — 45% of turns taken within the hour, some after a
night or a workday:

### Strict turn order doesn't work asynchronously

With one player moving at a time and everyone else waiting, **wall-clock duration
is the sum of every response delay in the game.** A 6-player game is 126 turns,
so even quick responses compound:

| Players | Strict order | Pipelined | Round-based |
| --- | --- | --- | --- |
| 2 | 8.2 days | **5.4 days** | 6.7 days |
| 3 | 12.3 days | **6.3 days** | 8.7 days |
| 4 | 16.4 days | **7.1 days** | 10.1 days |
| 6 | **24.7 days** | **8.5 days** | 12.3 days |

*(median duration, 21 turns each, 24h auto-play timeout)*

Nearly a month for a 6-player game is not a game anyone finishes. Strict
sequencing was the right call for a single live session; asynchronously it
collapses, because every player's idle time is additive rather than overlapping.

### Pipelined turn order

**Proposal — keep turn order, but let players run ahead.** A player may take
turn *k* as soon as both their own turn *k−1* and the previous player's turn *k*
are complete. Turn order is fully preserved — you never move before the player
ahead of you on the same round — but a responsive player isn't held hostage by a
slow one, since their waiting overlaps instead of stacking.

This is a **2.9x improvement** over strict sequencing at 6 players (8.5 days vs.
24.7) and beats round-based scheduling too, because round-based waits for the
slowest player every single round while pipelining lets fast players bank a lead.

It's a refinement of the sequential decision rather than a reversal: the rule is
still "players take turns in order."

### Timeouts

No shot clock, per the design intent. But a player who stops playing entirely
would otherwise stall the game forever, so some backstop is needed. Modelled:

| Auto-play timeout | 6-player median | p90 | Turns auto-played |
| --- | --- | --- | --- |
| None | 14.7 days | 17.8 days | 0% |
| 48h | 14.7 days | 17.8 days | 0% |
| **24h** | **12.3 days** | 14.0 days | **4.1%** |
| 12h | 8.9 days | 9.6 days | 14.7% |

*(round-based figures; the pattern holds for pipelined)*

**Proposal: a 24-hour auto-play timeout.** It's generous enough to be invisible
to real players — it fires on about **4% of turns** — while cutting ~2.5 days off
a 6-player game and guaranteeing games terminate. A 48h timeout is effectively no
timeout at all; a 12h one starts playing the game for people.

When it fires, it should take the *least destructive* default: first option on an
action tile, decline on optional life events, no investment change. Never
auto-play a decision that can't be recovered from.

### Board length

Async play removes the patience ceiling on board length — nobody is sitting
through a 60-minute session — and replaces it with a calendar ceiling:

| Board | Turns each | 6-player median | p90 | Games over 14 days |
| --- | --- | --- | --- | --- |
| 48 tiles | 14 | 8.2 days | 9.6 days | 0% |
| 60 tiles | 17 | 10.0 days | 11.5 days | 0% |
| **72 tiles** | 21 | 12.3 days | 14.0 days | **10%** |
| 96 tiles | 27 | 15.8 days | 17.7 days | 88% |

These figures assumed the old 72-tile placeholder. The board is now intended
to be **longer**, so a committed player can max a skill tree — which means
*more turns*, which stretches async duration unless action tiles resolve as
STOP spaces instead of extra spinner hops. That tradeoff is
[Q4](08-open-questions.md#q4--how-do-we-get-enough-action-landings).

Lobby size still changes the commitment more than anything else. Show an
estimated duration at lobby creation.

## The shared HUD

**Spec.** An interface available to all players during the game showing player
age (how far along the board they are), job title, house owned, number of
children, etc.

**Proposal — full transparency.** The HUD always shows every player's public
state, regardless of board distance:

| Field | Shown |
| --- | --- |
| Age | Derived from board position |
| Job title | Career + stage (e.g. *Senior Architect*) |
| House | Card name, not sale value |
| Children | Count and how acquired |
| Cash | **Open: see below** |
| Stats / perks | **Open: see below** |

Board games are information-open by nature, and in async play the HUD is the main
way you stay connected to a game you only touch once or twice a day. But total
transparency removes any surprise from the final reveal, and the
hidden-information question matters more here than in the original because builds
are so divergent.

Async play cuts both ways on this. Players have hours between turns, so anyone
inclined to optimize can do the arithmetic properly — which argues for
transparency, since hiding information from a determined player mostly just
punishes casual ones. But it also means a two-week game needs a payoff at the
end.

**Settled — you see how a life looks, not how it's going.**

| Public (openable lives sheet) | Hidden until retirement |
| --- | --- |
| Age / board position | Cash |
| Job title + stage | Salary |
| House name (not sale value) | Investments |
| Married / partner | Karma |
| Children (count, not how acquired) | Exact stat values and perk list |

The lives sheet is always available, separate from the turn recap. Recap is
"what happened while you were gone"; the sheet is "where is everyone right
now." Together they replace live spectating.

## The turn recap

**Async play needs something the live-session design didn't.** With days between
your turns, you open the app having missed everything — so the first thing you
see can't be a spinner. It has to be *what happened while you were gone*.

**Proposal — a recap screen on open:**

- Which players moved, how far, and what landed on them.
- Anything that happened to *you* in your absence (investment returns applied at
  a payday, a loan called).
- Who passed you or fell behind, tied to the proximity rule below.
- Then, and only then, your turn.

This is the retention mechanism for multiplayer, and it's worth saying plainly
because an earlier version of this doc had it wrong: in a live session the
argument was that spectating keeps a lobby engaged, so the camera and HUD carry
the experience. **Asynchronously, nobody spectates — there's nothing to watch,
because other players move while you're not looking.** The recap replaces
spectating entirely, and the 3D presentation earns its keep by making the recap
worth opening (short replays of other players' moments) rather than by making
waiting bearable.

## Proximity visibility

**Spec.** Players can see other players when within 10 tiles; otherwise they're
out of sight.

**Proposal — this is a rendering rule, not an information rule.** The 10-tile
radius governs whether another player's character appears in your 3D view. The
HUD is unaffected. So you always know where everyone is on the board; you just
don't see them on the road beside you unless they're close.

Read that way the two specs don't conflict, and the rule earns its place: passing
someone, or having someone pull alongside, becomes a visible moment. It also
conveniently caps how many characters need rendering at once, which matters on
mobile ([doc 07](07-art-and-presentation.md)).

In async play this is also good **recap material** — "you passed Sam while you
were away" is exactly the kind of beat that makes opening the app rewarding.

**Undefined:** does proximity enable any *interaction* — trades, favors, Buds
stat effects for travelling near others? There's an obvious hook here given a
whole stat is about friendship, and right now Buds has no inter-player
expression at all. See
[Q10 in doc 08](08-open-questions.md#q10--should-proximity-enable-interaction).

## Notifications

Async play means notifications aren't a feature, they're the delivery mechanism.
Getting them wrong either kills the game (nobody comes back) or gets the app
muted (same outcome, slower).

**Proposal — only three kinds:**

| Notification | When | Why |
| --- | --- | --- |
| **Your turn** | Turn becomes available | The only essential one |
| **Something happened to you** | Laid off, promoted, loan called while away | Events you didn't choose and would want to know about |
| **Game finished** | Final standings ready | Closes the loop on a two-week commitment |

Deliberately excluded: per-move notifications for other players. In a 6-player
game that's 105 notifications you didn't ask for, and it's the fastest route to
being muted. Other players' moves belong in the recap, not the lock screen.

One nudge before the 24h auto-play fires is probably worth it — at roughly
18 hours — so the timeout rarely surprises anyone.

## Logistics

Async play settles some of these by force:

- **Online, server-authoritative.** Not a choice any more: state has to persist
  for two weeks across six devices. Pass-and-play is off the table for the async
  mode (though it would work fine for solo).
- **Board layout and season decks are fixed at game creation** and shared by the
  lobby, so everyone plays the same board. With async play they also have to be
  *stored*, not generated per device.
- **Abandonment is handled by the 24h auto-play timeout** rather than by
  detecting disconnects — there's no connection to lose.

Still undecided:

- Lobby/invite flow; joinable by code or link.
- Can a player be added after a game starts? (Almost certainly not — the board
  position gap would be unrecoverable.)
- What happens if a player quits outright: auto-play to the end, or remove them
  from standings?
- Can one player be in several games at once? (Likely yes, and it's the main
  thing that makes a multi-day cadence sustainable.)
- Is there a "nudge" to prompt a slow player, and can it be abused?
