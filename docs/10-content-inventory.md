# 10 — Content Inventory

What has to be authored before the game has a soul. Mechanics can stay in the
design docs; this is the *stuff players read*. Lists themselves live in
[`content/`](content/README.md). Status: **empty shells + examples**, ready to
fill.

Your original list is the core. Everything else is either a sibling of those
lists, or a gate on them.

## The six you named

| List | Where | Working target | Why that size |
| --- | --- | --- | --- |
| Action tiles | [action-tiles.md](content/action-tiles.md) | ~160 cards (40 per season) | ~30 landings/run × 2× deck so games don't repeat, plus gated family cards |
| Outcome tiles | [outcome-tiles.md](content/outcome-tiles.md) | ~100 cards (25 per season) | Same 2× logic; smaller because they don't branch |
| Careers | [careers.md](content/careers.md) | ~17 (6 / 6 / 5 by education tier) | Distinct pools per path; some tier-3 are "enhanced" tier-2 |
| Houses | [houses.md](content/houses.md) | ~18 (6 per price band) | Draw 3 from the deck; 18 means the trio is actually random |
| Positive perks | [perks.md](content/perks.md) | 12 (4 tiers × 3 stats) | End-game bonuses only |
| Negative perks | [perks.md](content/perks.md) | 12 (4 tiers × 3 stats) | In-run, swingy |

Action tiles are the job. At two options each, ~160 cards is ~320 lines of
choice text. Everything else on this page is smaller than that.

## What the original list was missing

| List | Where | Target | Notes |
| --- | --- | --- | --- |
| **Board sequence** | still in [doc 03](03-board-and-tiles.md) | 1 layout | Which tiles are salary / action / outcome / STOP, and in what order. Can't size the decks until Q4 (how actions resolve) is picked |
| **Mid-life crisis deck** | [midlife-crises.md](content/midlife-crises.md) | 8–12 | Mandatory, karma-gated. Not an outcome tile |
| **Life event scripts** | [family.md](content/family.md) + [doc 04](04-life-events.md) | 6 events | University, marriage, house picker, children ×2, retirement — the UI flow and choices, not flavor sentences |
| **Gated family tiles** | mixed into action/outcome lists | ~20 married, ~20 parent | Same format as normal tiles, with a `gates` flag. This is how marriage and children get texture |
| **Career stage perks** | on each career row | 2 per career (Senior, Exec) | Without these, careers are salary numbers wearing hats |
| **Character cosmetics** | later; spec in [doc 02](02-character-and-stats.md) | styles × colors | Mechanical-zero; can wait until art |

Deliberately **not** a content list yet: investment return table (a formula),
notification copy, recap templates, scenery prop lists. Those wait until
rules and these lists exist.

## Suggested fill order

Order is about dependencies, not importance.

1. **Perk skeletons** — name and one-line effect at each ±25/50/75/100, even
   if numbers get retuned. Tile authors need to know what "going deep Brawn"
   *does*, or every action is flavor with no aim. **← current job**
2. **Career list** — titles, tiers, salaries, Senior/Exec perk. Unlocks
   university as a real choice and gives the HUD something to show.
3. **House list** — name, band, price, sale range. Small and self-contained.
4. **Action tile voice** — 8–10 finished examples per season (already started)
   to lock tone, then bulk-write. Write same-stat pairs first (marathon /
   couch), then split-stat pairs.
5. **Outcome tiles** in parallel with (4) — faster to write, good for filling
   season gaps.
6. **Mid-life crises** once karma's range is decided ([Q1](08-open-questions.md#q1--how-does-karma-work-as-a-separate-resource)).
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
