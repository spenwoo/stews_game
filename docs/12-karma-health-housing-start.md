# 12 — Karma, health, housing, and the start of a life

Working proposals for the five things in play while perks / careers / houses
are being listed in Excel. Numbers are starting points. **Spec** / **Settled**
mean we should not re-open them without a reason; **Proposal** is here to be
argued with.

---

## 1. Karma

**Settled.** Karma is a **separate currency**, not a stat and not a 0–100
meter. No cap, no floor, no "normalized" band. It goes up and down by the
amounts on tiles and events, and it can sit at +7 or −240 or +1,100.

Other players **never see it**. Hidden on the lives sheet with cash, salary,
and stats. That's the point: two lives that look the same on the HUD can
finish far apart because of a currency nobody else could track.

### Start and movement

| | Rule |
| --- | --- |
| Start | **0** |
| Cap | **None.** Positive and negative both unbounded |
| Visible to you | Yes, on your own sheet |
| Visible to others | **No** |

| Source | Typical delta |
| --- | --- |
| Outcome tiles | whatever the card says (can be large) |
| Action-tile riders | whatever the card says |
| Bank loan | −5 |
| Missed mortgage | −8 |
| Adoption | +15 |
| College-for-kid | +10 |

No clamping after a hit. If a tile says −40, you go −40 from wherever you
were.

### Where it pays

Karma is **end-game variance**, plus one mid-run read:

| When | What it does |
| --- | --- |
| **Retirement score** | Added to the estate as a hidden line. Proposal: **$1,000 per karma point**, no cap — so a saint and a villain with the same house can land very different totals. **Enlightened** still triples this if active |
| **Mid-life crisis** | Sign and size still flavor the table (positive vs negative; bigger number = stronger version). Not a 0–100 gate |
| **Child legacy** | Scales "how they turned out" with your karma total, for the same reason |

Because it's uncapped, a linear score *can* dominate a close lobby. That's
accepted — it's the fog. If playtests show one karma tile swinging the
whole match, shrink the per-point dollar amount, not the currency.

---

---

## 2. Health ailments

**Settled: three, different rules.** You can hold more than one at once.
Hidden from other players (recap names it for you). **Roid Rage** clears
whatever you have and blocks new rolls while that perk is active.

Checked **once per spin** (every time you throw the spinner), except as
noted.

### Chronic joint pain

| | Rule |
| --- | --- |
| Chance | Starts **low**, rises as you move through the board. Proposal: `2% + 10% × (tiles_passed / board_length)` per spin, so ~2% in youth and ~12% at retirement |
| Cost | **$1,000** flat, every payday, labeled physical therapy |
| Cure | Does not self-cure. Roid Rage clears it. (A paid medical tile can also clear it if we author one.) |
| If you already have it | Don't roll again |

### Cancer

On infliction, randomly assign a type — **bone, skin, lung, throat, or
pancreatic** — flavor only, same math.

| | Rule |
| --- | --- |
| Chance | **2% per spin** |
| Cost | **50% of every payday** (half the salary you would have collected on that tile) |
| Cure | **5% per spin** to clear, rolled after movement. Recap: "in remission" |
| If you already have it | Don't roll a second cancer; keep rolling the 5% cure |

Over ~40 spins, about **55%** of players see cancer at least once. Then 5%
per spin to get rid of it — expected wait ~20 spins if you never hit Roid
Rage. Half-pay for that stretch is the teeth.

### Alzheimer's

| | Rule |
| --- | --- |
| Window | **Only after 25% of the board** (the last 75% of tiles). Youth and early career are immune |
| Chance | Not specified — proposal **2% per spin** once the window is open, same as cancer, so it isn't a joke and isn't guaranteed |
| Cost | **25% of every payday** |
| Agency | **No action-tile choices.** When you land on an action tile, the game picks an option at random and resolves it. You see the result after |
| Cure | Does not self-cure. Roid Rage clears it and restores choice |

This is the harshest of the three: money *and* the lifestyle-commitment
system go fuzzy. That's the point. If 2%/spin in the last 75% feels like
too many Alzheimer's runs in a 6-player lobby, we drop the rate before we
drop the effect.

### Perk interactions

| Perk | Joint pain | Cancer | Alzheimer's |
| --- | --- | --- | --- |
| **Roid Rage** | Clears + blocks | Clears + blocks | Clears + blocks, choices return |
| **Lifer** | First ailment roll this run is ignored (any of the three) | same | same |
| **Ignorant** | Infliction chance +10% while active; +$10k/payday only while you have none | same | same |
| **Sickly** | Once: pass your current ailment to a chosen opponent, silently | same | same |
| Mid-life health scare | Separate one-shot crisis, also blocked by Roid Rage | | |

---

## 3. Homeownership

**Settled direction** from the housing notes. Card list, prices, hidden perks,
and rentals: [content/houses.md](content/houses.md).

Every player is always either a **homeowner** or a **renter**. There is no
homeless state. Housing tiles (**four** — House I–IV) are the only places you can acquire a
house or move up. Selling can happen at any time.

House and rental **perks are hidden until purchased**. The draw shows name
and price only.

### Buy: cash or mortgage

On a housing tile, if you own no house, draw **3** remaining exclusive cards.
Pick one, then choose:

| Path | Rule |
| --- | --- |
| **Cash** | Pay the full list price. The house is yours for the rest of the run unless you sell or move. No payday draft, no grace, no foreclosure. Total paid = **100%** of list |
| **Mortgage** | Pay **20% of list price** up front. That payment is **implicit interest** — it does **not** reduce the balance. The **full table value** is then split into **20 equal payday drafts**, auto-taken when you cross a payday tile, until the entire list is paid down. Total paid = **120%** of list |

Cash is cheaper if you can fund the sticker. Mortgage is the liquidity
route, and the 20% is the tax for not having the cash.

If you cannot cover the cash price or the 20% down, you cannot take that
path on this card — cheaper card, the other path, a rental, or a bank loan
first.

Married: housing costs **double** like every other cost.

You may **decline the draw** and pick a rental instead. That is how a run
starts as a renter; later housing tiles still let you buy if you own none.

### Missed payments — two grace periods, then foreclosure

Mortgage payment is automatic. If the bank cannot cover it:

1. The missed amount stays as **arrears**.
2. You spend one of **two grace periods** on this mortgage (karma −8, same
   as the old missed-mortgage line).
3. The next payday tries to collect current payment **plus** arrears.

If a payment comes due with **both grace periods already used** and the bank
still cannot cover it, **foreclosure is automatic**:

- House returns to the exclusive pool.
- Remaining mortgage is wiped. You keep **no equity**.
- You must immediately pick a rental.

Grace periods reset when the mortgage is paid off, sold, or replaced by a
move. Cash buyers never enter this system.

The old "half equity back" and "principal ÷ paydays left" schedules are
**superseded**.

### Appreciation

**Settled — shared spin market, calmer than investments.** Every spinner
result in the lobby moves **every owned house** by the same percentage.
Rentals do not appreciate. One-off tile shocks (later) can hit housing,
the stock market, or both.

| Spin | Effect | Odds |
| --- | --- | --- |
| 1 | −0.25% | 1/6 |
| 2 | 0.00% | 1/6 |
| 3 | +0.15% | 1/6 |
| 4 | +0.20% | 1/6 |
| 5 | +0.25% | 1/6 |
| 6+ | +0.35% | 1/6 |

Expected value **+0.117% per spin**, **+0.70% per round** in a 6-player
lobby. Only a 1 loses money. Solo stays on the quieter per-spin curve — no
ghost rolls.

Same % on every house means a $600k Mega Mansion still makes more *dollars*
than a $60k houseboat without needing a wilder table. **Estate Minded**
doubles whatever this table rolled for that player's house only (booms and
crashes).

A house bought ~40% into a 6p game (House I) sees roughly **+10% to +29%**
by retirement depending on board length (~$25k–$74k on a $260k ranch). That
can approach the 20% mortgage interest in a long 6p game; cash is still
cleaner if you can pay the sticker. Full market comparison:
[doc 05](05-economy-and-investments.md#balance-vs-current-salaries).

At retirement (or sale):

```
estate housing = current value − remaining mortgage
```

Rentals contribute $0 here. They only cost their payday rent.

### Selling

Allowed **at any time** from the lives sheet.

- Sale price = **current value** (purchase price + appreciation).
- Remaining mortgage (unpaid share of the **full list**, not list minus the
  down payment) comes out of proceeds first. The 20% down was never equity.
- Leftover cash is yours. Sell at close with no appreciation and leftover is
  **$0**.
- Card returns to the exclusive pool.
- You **must** pick a rental immediately.
- You may buy again at a later housing tile if you still own none.

### Moving (later housing tiles only)

If you already own a house, the tile offers **stay** or **move**. Move
draws 3 remaining houses with **greater list price** than your current one.

| | Rule |
| --- | --- |
| Move cost | Flat **$10k** (**Starter Home** waives this) |
| New mortgage | `remaining mortgage + (new list − old list)`, then **reset** that balance across the **next 20 paydays**, payments recalculated. No second 20% interest fee — that fee is only on a financed purchase |
| Cash owners | Remaining mortgage is $0, so the value gap becomes the new 20-payment mortgage at face value. Still pay the $10k |
| Perk | Old perk ends; new perk reveals on purchase |
| Old card | Returns to the pool |

You cannot move down in list price on these tiles. To leave without
upgrading, sell and rent.

### Rentals

Five options, rent charged on every payday crossing. Not exclusive. Perks
hidden until chosen, except Studio's child gate is enforced at pick time.

| Rental | Rent / payday | Perk |
| --- | --- | --- |
| Parents Basement | $0 | abs(Buds) pulled 50 toward 0, floor 0 |
| Motel Room | $10k | +5% layoff chance |
| Studio Apartment | $20k | Cannot pick if you have children |
| Hotel Suite | $30k | abs(Brawn) pulled 20 toward 0, floor 0 |
| Rental House | $40k | No debuff |

### Why expensive houses are scary

- The 20% down is a sunk interest fee, then you still draft the full list
  over 20 paydays (120% total vs cash at 100%)
- Fatter 1/20 payday draft (full list ÷ 20, not 80% ÷ 20)
- Appreciation is the same % on every house (dollars scale with price; Estate Minded doubles your rolls)
- Two missed paydays and you lose the asset with no equity back
- Married doubles the down payment, the payday draft, the $10k move, and rent

Cheap house / cash buy: you can actually hold it. Premium + mortgage: you
are levered for twenty paydays.

---

## 4. Youth stretch, then college

University is **not** tile 0. The game opens on a short **youth** stretch so
Brains (and the other two) can move *before* the school door.

**Proposal:**

| | Value |
| --- | --- |
| Youth tiles | **19** (summer flavor: school-age, first job, friends, habits) |
| Then | **University STOP** (mandatory) |
| Then | No-school → career, or undergrad track, optional grad |

With land-only actions and a 1–6 spinner that's about **3–5 action landings**
before the door. At X=10 that's enough to swing Brains by **±10 to ±40** on
top of your nature. A Scholar who then picks every "snack on the couch" can
still miss the good schools. A Jock who hits the study tiles can still get in.

### What Brains unlocks at the STOP

Always available: **no school**. Named campuses, six undergrad tiers, and
grad-capable flags are in [content/schools.md](content/schools.md). Sticker
prices there **replace** the old flat $80k / $100k.

| Brains at the stop | Undergrad door (proposal, mapped onto the sheet) |
| --- | --- |
| < 0 | PUB3 / PR3 only (open admission — still "undergrad" for college-gated jobs) |
| ≥ 0 | PUB2 / PR2 also in the draw |
| ≥ +25 | PUB1 / PR1 also in the draw. **Collegiate** weights these up further |

Grad school is a **$100k** add-on drawn from campuses marked `grad`. Own
Brains check (proposal: ≥ +15 from wherever you are then). **Accredited**
can grant a grad degree later for $20k if you already have undergrad.

---

## 5. Opening class / nature

Replaces the old "10 points at creation" idea. **Settled direction:** one
class per permutation of **+15 / −15**, plus one true neutral.

Three stats → **6 named natures + 1 neutral = 7**.

| Class | +15 | −15 | Early hook (so Brains isn't the only smart pick) |
| --- | --- | --- | --- |
| **Scholar** | Brains | Brawn | School doors. You already sit on the State line; Selective is one good tile away |
| **Pretentious** | Brains | Buds | School doors, but colder start (divorce risk later if you stay low Buds) |
| **Jock** | Brawn | Brains | **Athletic scholarship:** if Brawn ≥ +10 at the University STOP, State school is available *even if Brains is below 0*, and tuition is **$40k** instead of $80k. Also: first `health` infliction this run is ignored |
| **Stoic** | Brawn | Buds | Same scholarship / health ignore. Worse Buds for the social / divorce side |
| **Charmer** | Buds | Brains | **Legacy letter:** if Buds ≥ +10 at the STOP, State school is available even if Brains is below 0 (full tuition). **Co-sign:** first education loan does **not** cost karma. No-school: offered **4** career cards instead of 3 |
| **Jolly** | Buds | Brawn | Same legacy / co-sign / extra career card. Worse Brawn for health |
| **Ambivalent** | — | — | All zeros. No hook, no hole. The control class |

Same-stat +15/−15 is **Ambivalent** — one name, not three.

Creation order: appearance → class → youth stretch → University STOP.

### Why this balances the Brains rush

Without extra doors, everyone would pick Scholar/Pretentious, farm one study
tile, and walk into Selective. The other classes get **alternate keys** to
the same building:

| Door | Who it's for | What you pay |
| --- | --- | --- |
| Grades (Brains) | Scholar / Pretentious | Time on study tiles, maybe full tuition |
| Scholarship (Brawn) | Jock / Stoic | Half tuition, but you had to *keep* Brawn up through youth |
| Legacy (Buds) | Charmer / Jolly | Full tuition, no karma on the first loan, better no-school backup |

No-school is still the liquidity play. Charmer makes it *better* (4 career
cards from the exclusive pool — first dibs on a job without sitting in class).
Jock makes "I went to school anyway" cheaper. Scholar makes the *good*
school available. Three different reasons to exist in the first twenty
minutes.

Youth tiles should include a mix of Brains / Brawn / Buds actions so a Jock
isn't forced to dump their +15 on snack tiles. That's an authoring note for
the summer-youth slice: **at least two same-stat cards per stat** in that
stretch.

---

## What landed from the Excel

Copied into `docs/content/` (working copies — `data_files/` is not edited
from here):

- [perks.md](content/perks.md) — 48 names/effects
- [careers.md](content/careers.md) — 47 titles, stage mids, special perks
- [houses.md](content/houses.md) — 29 houses + 5 rentals, hidden perks
- [schools.md](content/schools.md) — named campuses and tier tuition

Still open:

- [ ] Karma: $1,000/pt uncapped at retirement — too spicy once Enlightened exists?
- [ ] Alzheimer's infliction rate (proposal 2%/spin after 25% of the board)
- [x] Youth length 19 tiles
- [ ] Scholarship $40k and legacy-at-full-tuition as the Brawn/Buds keys, now
      that undergrad stickers are $70k–$240k
- [x] Four housing tiles (House I–IV)
- [ ] Five salary bands vs the sheet's "±1 extra level" note
