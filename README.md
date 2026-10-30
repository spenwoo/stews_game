# Stew's Game

A reimagined take on the classic board game *The Game of Life* — same turn-based
journey along a board, but with a deeper decision layer, a stat/perk system that
rewards risk, and a longer, more varied arc from school through retirement.

Solo is a single ~10 minute sitting played for score. Multiplayer is
**asynchronous over days**: up to 6 players, notified when it's their turn, no
shot clock.

**Status: design phase.** No gameplay code yet. The goal right now is to pin down
mechanics and balance before anything gets built.

**Coming back later?** Open [docs/11-pickup-checklist.md](docs/11-pickup-checklist.md).
Next job: perk names.

## Design docs

| Doc | Covers |
| --- | --- |
| [01 — Design Overview](docs/01-design-overview.md) | Pitch, design pillars, what's different from the original |
| [02 — Character & Stats](docs/02-character-and-stats.md) | Creation screen, the stat system, perk tiers |
| [03 — Board & Tiles](docs/03-board-and-tiles.md) | Board layout, tile types, movement, seasons |
| [04 — Life Events](docs/04-life-events.md) | University, career, marriage, house, children, mid-life crisis |
| [05 — Economy & Investments](docs/05-economy-and-investments.md) | Money, salaries, the investment account, loans, final scoring |
| [06 — Modes & Multiplayer](docs/06-modes-and-multiplayer.md) | Solo vs. multiplayer, turn flow, the shared HUD, visibility |
| [07 — Art & Presentation](docs/07-art-and-presentation.md) | Visual direction, camera, mobile constraints |
| [08 — Open Questions](docs/08-open-questions.md) | Unresolved decisions and known conflicts in the spec |
| [09 — Balance Model](docs/09-balance-model.md) | Simulation results: perk parity, education, marriage, children |
| [10 — Content Inventory](docs/10-content-inventory.md) | What to author, in what order, and how big |
| [11 — Pickup checklist](docs/11-pickup-checklist.md) | Settled rules, open questions, content still to write |
| [Content lists](docs/content/README.md) | Action tiles, outcomes, careers, houses, perks, crises, family |

## Reading the docs

Anything written as **Spec** came directly from the original concept and is
treated as settled. Anything written as **Proposal** is a starting number or
mechanic invented to make the system concrete — it exists to be argued with and
tuned, not to be treated as final. **Settled** means it was open and has since
been decided. Open questions are collected in doc 08 and cross-referenced from
wherever they come up.

## Models

Two things in this design can't be settled by argument, so they're modelled.
Re-run these whenever a number changes; the figures quoted in the docs come from
them.

**[`tools/balance_model.py`](tools/balance_model.py)** — Monte Carlo model of the
rules at the level of money and stats. The central risk/reward system has two
dials (how much negative perks pay during a run, how much positive perks multiply
at the end) that have to be solved against each other. Prints eight findings
covering perk reachability, positive/negative parity, education, marriage,
children, and stat count.

```
py tools/balance_model.py --runs 20000
```

**[`tools/async_pacing.py`](tools/async_pacing.py)** — how long an asynchronous
multi-day game actually takes, given realistic response latency. Compares strict,
pipelined, and round-based turn scheduling, and sizes the auto-play timeout.

```
py tools/async_pacing.py
```

**[`tools/check_links.py`](tools/check_links.py)** — verifies every internal doc
link and heading anchor still resolves.
