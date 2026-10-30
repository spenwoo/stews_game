# Houses

At the house event the player is offered **3 random cards** from this deck.
They pick one. Open: can they decline entirely? (see [doc 04](../04-life-events.md#buy-a-house)).

Sale value is rolled at retirement inside the range — housing is an investment
with spread, not a fixed number.

| Column | Meaning |
| --- | --- |
| id | Stable handle |
| name | Player-facing |
| band | starter / mid / premium |
| price | Purchase cost (not doubled extra rules beyond marriage) |
| sale_low | Worst retirement sale |
| sale_high | Best retirement sale |
| tags | Optional: `family` (better with children), `fixer`, `city`, `quiet` |
| notes | |

Bands from [doc 04](../04-life-events.md#buy-a-house): starter ~$120k,
mid ~$250k, premium ~$450k. Prices can vary inside the band so the three
drawn cards aren't clones.

Target: **6 per band, 18 total.**

---

## Starter

| id | name | price | sale_low | sale_high | tags | notes |
| --- | --- | --- | --- | --- | --- | --- |
| h-s1 | The Walk-Up | 110000 | 90000 | 160000 | city | |
| h-s2 | Starter Ranch | 120000 | 100000 | 180000 | quiet | |
| h-s3 | The Fixer | 95000 | 70000 | 190000 | fixer | High variance |
| h-s4 | Duplex Half | 130000 | 110000 | 175000 | | Rent flavor later? |
| h-s5 | Cabin-ish | 115000 | 85000 | 170000 | quiet | |
| h-s6 | Condo Cube | 125000 | 100000 | 165000 | city | |

## Mid

| id | name | price | sale_low | sale_high | tags | notes |
| --- | --- | --- | --- | --- | --- | --- |
| h-m1 | The Colonial | 240000 | 200000 | 360000 | family | |
| h-m2 | Brick Rowhouse | 260000 | 210000 | 370000 | city | |
| h-m3 | Split-Level | 230000 | 190000 | 340000 | | |
| h-m4 | Craftsman | 270000 | 220000 | 380000 | | |
| h-m5 | Lake Street | 250000 | 200000 | 355000 | quiet | |
| h-m6 | The Addition | 255000 | 180000 | 390000 | fixer family | |

## Premium

| id | name | price | sale_low | sale_high | tags | notes |
| --- | --- | --- | --- | --- | --- | --- |
| h-p1 | Glass Box | 480000 | 360000 | 720000 | city | |
| h-p2 | The Acreage | 450000 | 350000 | 700000 | quiet family | |
| h-p3 | Downtown Pent | 520000 | 380000 | 740000 | city | |
| h-p4 | Restored Victorian | 440000 | 330000 | 710000 | fixer | |
| h-p5 | Architect's Own | 470000 | 340000 | 730000 | | |
| h-p6 | Family Compound | 490000 | 370000 | 760000 | family | Extra score if parent? |

**Still open:** ongoing upkeep per payday, decline-to-buy, upgrade later,
married players seeing a 4th `family` card.
