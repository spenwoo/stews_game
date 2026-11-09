# 10 — Content Inventory

What has to be authored before the game has a soul. Mechanics can stay in the
design docs; this is the *stuff players read*. Lists themselves live in
[`content/`](content/README.md). Status: perks, careers, houses, and schools copied from
`data_files/Life Data File.xlsx`. Action/outcome tiles still examples.

Your original list is the core. Everything else is either a sibling of those
lists, or a gate on them.

## The six you named

| List | Where | Working target | Why that size |
| --- | --- | --- | --- |
| Action tiles | [action-tiles.md](content/action-tiles.md) | ~160 cards (40 per season) | ~30 landings/run × 2× deck so games don't repeat, plus gated family cards |
| Outcome tiles | [outcome-tiles.md](content/outcome-tiles.md) | ~100 cards (25 per season) | Same 2× logic; smaller because they don't branch |
| Careers | [careers.md](content/careers.md) | **47** (no-school / college / college+grad) | Education flags and stage mids from the sheet |
| Houses | [houses.md](content/houses.md) | **29** houses + **5** rentals | Draw 3; perks hidden until purchased |
| Positive perks | [perks.md](content/perks.md) | 24 (4 tiers × 3 stats × 2 picks) | Mix of in-run and retirement |
| Negative perks | [perks.md](content/perks.md) | 24 (4 tiers × 3 stats × 2 picks) | In-run, swingy |

Action tiles are the job. At two options each, ~160 cards is ~320 lines of
choice text. Everything else on this page is smaller than that.

## What the original list was missing

| List | Where | Target | Notes |
| --- | --- | --- | --- |
| **Board sequence** | [tiles/board.md](content/tiles/board.md) + [tiles/board-slots.csv](content/tiles/board-slots.csv) | 1 layout, ~369 walked squares | Six short forks; ~75% spine. Slot types fixed; card text shuffles from the CSVs |
| **Mid-life crisis deck** | [midlife-crises.md](content/midlife-crises.md) | 8–12 | Mandatory, karma-gated. Not an outcome tile |
| **Life event scripts** | [family.md](content/family.md) + [doc 04](04-life-events.md) | ~12 events | University, career, marriage, House I–IV, children ×3, mid-life, retirement |
| **Gated family tiles** | mixed into action/outcome lists | ~20 married, ~20 parent | Same format as normal tiles, with a `gates` flag. This is how marriage and children get texture |
| **Career special perks** | on each career row | 1 per career | Sheet left some blank; fill those |
| **Schools** | [schools.md](content/schools.md) | ~70 named campuses | Six undergrad tiers + $100k grad add-on |
| **Character cosmetics** | later; spec in [doc 02](02-character-and-stats.md) | styles × colors | Mechanical-zero; can wait until art |

Deliberately **not** a content list yet: investment return table (a formula),
notification copy, recap templates, scenery prop lists. Those wait until
rules and these lists exist.

## Suggested fill order

Order is about dependencies, not importance.

1. **Perk skeletons** — copied from the Excel. Review names/effects, then
   bulk-write tiles against them.
2. **Career list** — copied. Fill blank special perks; retune education doors
   against the new salary mids.
3. **House list** — copied, plus rentals and the cash/mortgage rules.
4. **Action tiles** — voice is locked; fill [tiles/actions.csv](content/tiles/actions.csv)
   strip by strip (youth, then college/work, then the rest). At least as
   many cards as action slots on that strip. Spine is now the bulk of the work.
5. **Outcome tiles** in parallel — [tiles/outcomes.csv](content/tiles/outcomes.csv).
   ≥8 cards per fork side.
6. **Mid-life crises** (karma is an uncapped hidden currency now; crisis still
   reads the sign and size).
7. **Family-gated cards and event scripts** last, because they reference the
   other lists (spouse careers, house bands, parent-only spring tiles).

## Authoring rules that apply to every list

- Season-tag everything that appears on the board. A winter card never draws
  in summer.
- One effect per card. If you want two things to happen, that's two cards.
- Money amounts live on a small ladder so they stay tunable as a set:
  **$0 / $2k / $5k / $10k / $25k / $40k** for tiles. Life events can go
  bigger.
- No proper names of real brands. No punchlines that date in a year.
- Gated cards declare their gate (`married`, `parent`, `no_children`,
  `grad`) rather than living in a separate secret list — keeps the season
  decks in one place.

## Open sizing questions

These change how big the lists need to be. Don't bulk-write past the examples
until they're picked.

- [Q4](08-open-questions.md#q4--how-do-we-get-enough-action-landings) — stop
  spaces vs. long board vs. pass-and-resolve.
- Default X = 10, or does it vary by season (smaller in summer, larger in
  winter)?
- Share of same-stat vs. split-stat action tiles. Proposal: **half and half**.
- Share of action tiles that also move money. Proposal: **about 40%**, and
  when they do, the good option is the expensive one.
