# 01 — Design Overview

## Pitch

You travel a fixed path from your school years to retirement, rolling to move,
collecting salary as you pass paydays, and resolving whatever tile you land on.
The familiar shape of *The Game of Life* is intact. What's new is that most tiles
ask you to *choose*, and those choices move five personal stats that unlock perks
in both directions — including deliberately tempting bad ones.

## Design pillars

**1. Every tile is a decision, not a dice outcome.**
The original is almost entirely passive: you spin, you move, you read what
happened to you. Here, action tiles present two life choices. You pick on
flavor — the stat that moves, and the direction, stay hidden until after.
Good actions raise a stat; bad ones lower one. Over a long board that
becomes a lifestyle, not a spreadsheet.

**2. The negative path is genuinely tempting.**
Negative perks are stronger *during* the run; positive perks used to pay only
at the end. The Excel list now mixes in-run and retirement effects on both
trees — the gamble is still "commit to a path," but the timing is per-perk.
See [content/perks.md](content/perks.md) and
[doc 05, Final Scoring](05-economy-and-investments.md#final-scoring).

**3. Early choices compound.**
University, career tier, marriage, and children all gate or multiply what's
available later. A decision at tile 8 should still be visibly shaping your
options at tile 60.

**4. Two cadences, one rule set.**
Mobile-first. Solo is a single sitting of ~10 minutes, played for score.
Multiplayer is **asynchronous and runs over days** — you're notified when it's
your turn, take it whenever, and put your phone away. Same rules, same board,
same scoring; completely different relationship with the player's time. See
[doc 06](06-modes-and-multiplayer.md#pacing-and-session-length).

## What's different from the original

| The Game of Life | Stew's Game |
| --- | --- |
| Peg in a car, no identity | Customizable 3D character, stat loadout |
| Outcomes are read off the tile | Most tiles are a two-option choice |
| No persistent character traits | Five stats, −100 to +100, with perk tiers |
| College or career, one fork | University → optional grad school → tiered careers |
| Career is fixed once drawn | Promotions to Senior/Executive, plus layoff risk |
| Money sits idle in the bank | Investment account with returns, risk, and loans |
| Winner = most money | Score blends money, assets, stats, and family |
| Static board | Seasons shift summer → fall → winter → spring |

## Scope boundary for this phase

In scope now: mechanics, numbers, balance, content lists (tiles, careers, houses,
crises), scoring.

Deliberately not yet: engine/framework choice, art pipeline, netcode, deployment.
Those get decided once the rules are stable.
