# Tile database

This folder is the working database for every square a player can land on.
Author here, not in `data_files/` (that folder is user-owned uploads).

| File | What it is |
| --- | --- |
| [board.md](board.md) | Human map: forks, gates, length |
| [board-slots.csv](board-slots.csv) | Every square, in order, with type |
| [actions.csv](actions.csv) | Action-tile text boxes (two options, hidden ±X) |
| [outcomes.csv](outcomes.csv) | Outcome-tile text boxes (no choice) |
| [../action-tiles.md](../action-tiles.md) | Voice rules (the CSVs are the list) |
| [../outcome-tiles.md](../outcome-tiles.md) | Voice rules (the CSVs are the list) |

Regenerate slots after changing the map sketch:

```
py tools/gen_board_slots.py
```

Do not hand-edit `board-slots.csv` if you can change `tools/gen_board_slots.py`
instead — the generator is the layout source.

---

## How a card gets onto the board

1. The board is a list of **slots** (`board-slots.csv`). Each slot has a
   `type` (`action`, `outcome`, `payday`, `stop`, `fork`) and a `draw_pool`
   (the branch or spine strip it belongs to).
2. At game start, each `action` / `outcome` slot draws a unused card from
   `actions.csv` / `outcomes.csv` whose `branch` matches `draw_pool`, then
   whose `season` matches, then any leftover season card. Gated cards
   (`married`, `parent`, `no_children`, `grad`) only draw if the flag is on.
3. **Payday** slots have no text box. Land or pass: collect salary (after
   the Career stop). Flavor can wait.
4. **Stop** / **fork** slots always halt. Scripts live in
   [doc 04](../../04-life-events.md) and [family.md](../family.md).

Two games on the same map shuffle differently. The *shape* is fixed; the
sentences are not.

---

## CSV columns

### actions.csv

| column | meaning |
| --- | --- |
| id | Stable handle. Never reuse. |
| season | summer / fall / winter / spring |
| branch | Draw pool: `youth`, `college`, `work`, a fork name, or a spine strip |
| pair | `same` or `split` |
| good_stat / bad_stat | brains / brawn / buds |
| X | Magnitude, default 10 |
| good / bad | Player-facing sentences |
| good_money / bad_money | Cash delta (negative = cost) |
| gates | blank, `married`, `parent`, `no_children`, `grad` |
| notes | Design intent, not player-facing |

Hidden until after the pick: stats, signs, amounts. Good always raises;
bad always lowers. See [action-tiles.md](../action-tiles.md).

### outcomes.csv

| column | meaning |
| --- | --- |
| id | Stable handle |
| season | summer / fall / winter / spring |
| branch | Draw pool |
| money | Cash delta |
| karma | Karma delta |
| text | One-liner |
| gates | blank or `married` / `parent` / `no_children` / `grad` |
| tags | optional `health` |
| notes | Design intent |

Money ladder: $0 / ±$2k / ±$5k / ±$10k / ±$25k / ±$40k.

### board-slots.csv

| column | meaning |
| --- | --- |
| slot_id | Unique square id |
| region | Fork or spine name |
| branch | Which side of a fork, or the spine strip |
| seq | 1…n along that strip |
| type | action / outcome / payday / stop / fork |
| season | summer / fall / winter / spring |
| draw_pool | Which CSV `branch` fills this square |
| stop_event | Life-event id if type is stop/fork |
| gate | Who may walk this strip |
| notes | |

---

## Authoring a new card

1. Add a row to `actions.csv` or `outcomes.csv`.
2. Set `branch` to the strip you want it to appear on (see [board.md](board.md)).
3. Keep one effect. Don't put two jokes in one box.
4. On a **stat-gated** fork, lean the *gated* side toward that stat
   (`same` pairs on the gate stat). Keep money EV close to the open side.
5. Fill until each action pool has at least as many cards as action slots
   on that strip. Spine strips are the bulk of the board. 2× is better so
   games don't repeat.

Current seed: 60 actions / 40 outcomes. Forks still need more rows — that's
the next fill job, strip by strip, starting with `youth` then `college` /
`work`.
