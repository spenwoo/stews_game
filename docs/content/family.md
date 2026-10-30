# Marriage & children — event scripts

Gated *tiles* live in the action/outcome lists with a `gates` flag
(`married`, `divorced`, `parent`, `no_children`). This file is the event
flows. Numbers in brackets are starting points, not locked.

---

## Marriage event

1. Choose: marry or stay single. (If single, skip the rest.)
2. Pick partner presentation: male / female. Cosmetic.
3. Pay wedding cost (**$15k**, *before* doubling starts).
4. Pick a spouse career from your education tier, same list as
   [careers.md](careers.md).
5. From this point, while together:
   - +50% of spouse salary every payday
   - **all costs double**
   - spouse payday-count tracks yours (Senior/Exec when you do)
   - spouse cannot be laid off
   - `married` tiles can draw
   - payday **divorce check** (see below)

**Together at retirement:** flat score bonus if still married at the end.
Proposal: **$80k**. Tune against the already-near-neutral money math.

Deferred: partner stat-lean, 4th family house card, anniversary stop.

### Divorce — Buds is the leak

Checked **once per payday** while married, and **again** if you pick the bad
option on a `married` action tile.

```
if Buds >= 0:  chance = 1% − Buds / 200            [floor 0.3%]
if Buds <  0:  chance = 1% + (|Buds| / 100) × 12%  [ceil 13%]
```

| Buds | Per check | Odds of ≥1 divorce over 10 paydays |
| --- | --- | --- |
| +100 | 0.3% | ~3% |
| 0 | 1% | ~10% |
| −25 | 4% | ~34% |
| −50 | 7% | ~52% |
| −100 | 13% | ~75% |

A committed negative-Buds life is more likely than not to end the marriage.
A well-liked one almost never does.

**Aftermath:**

- Spouse salary stops. Costs un-double from the next tile on.
- Legal cost **$20k** (not doubled — doubling just ended).
- Children stay. Upkeep and `parent` tiles continue.
- `married` tiles stop. `divorced` tiles may draw.
- Together-at-retirement bonus is lost.
- Lives sheet shows divorced. Recap tells the lobby.

A second path: mid-life crisis card `c-divorce`
([midlife-crises.md](midlife-crises.md)). Same aftermath, more drama.

---

## Children events (two stops)

Each stop:

1. Birth (~$10k) / Adoption (~$40k, karma up) / No child this time.
2. If yes, increment children. `parent` tiles can draw.
3. Second stop can still say no. Cap is 2 from these events unless we add
   more later.

**Value mix (settled):**

| Lever | Direction | Starting number |
| --- | --- | --- |
| One-time cost | Down | Birth $10k / adoption $40k (doubled if married) |
| Payday upkeep | Down | **$4k per child per payday** (doubled if married) |
| Karma on adoption | Sideways | +15, enough to matter at the crisis |
| Parent-only tiles | Sideways | Fall / winter / spring |
| College-for-kid | Down now, up later | Optional stop, ~$40k, karma + score |
| Legacy bonus | Up at retirement | Per child, scaled by karma and Buds |
| Spring slice | Different, not empty | Parents: grandkids/care. `no_children`: travel/mentor/second-act |
| "Your kid became X" | Recap | Weighted by stats + karma |

Kids survive divorce. Upkeep does not stop.

**College-for-kid** sits after Children II, before spring. Decline is allowed.
Paying is the positive-path-pays-later beat in miniature.

---

## Gated card quotas to write

Fold into the main action/outcome lists, don't make a secret second deck.

| Gate | Action | Outcome | Notes |
| --- | --- | --- | --- |
| `married` | ~12 | ~6 | Date night, in-laws, a fight. Bad option rolls divorce |
| `divorced` | ~4 | ~2 | Late-game, small slice |
| `parent` | ~16 | ~8 | School play, teenager, driving lessons |
| `no_children` | ~8 | ~4 | Spring travel / mentor / second act |
