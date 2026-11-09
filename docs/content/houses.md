# Houses and rentals

Copied from `data_files/Life Data File.xlsx` (Houses sheet). That folder is
user-owned — this file is the working copy. Do not edit the spreadsheet from
here.

Full buy / mortgage / sell / move / foreclosure rules:
[doc 12](../12-karma-health-housing-start.md#3-homeownership).

**Multiplayer: exclusive.** A purchased house leaves the lobby pool until it
is sold or foreclosed. Unchosen cards go back. Ahead players see a better
trio on average. Solo: full deck. Rentals are **not** exclusive — any number
of players may hold the same rental type.

**Perks are hidden until purchased.** The draw shows name and price only.
The perk (title, stat buff, spin bonus, and so on) is revealed after you
own it. Same rule for rentals.

Prices are list prices in the table. Current value is list price plus the
shared housing market (every lobby spin ticks every owned house — table in
[doc 12](../12-karma-health-housing-start.md#appreciation)). Sale price is
always current value. Rentals do not appreciate.

---

## How a housing tile works

There are **four** housing tiles on the board (House I–IV). On each:

| You currently… | The tile offers |
| --- | --- |
| Own no house | Draw **3** remaining houses. Pick one and **pay cash** or **mortgage**, or decline and pick a **rental** |
| Already own a house | Stay, or **move**: draw 3 houses whose list price is **greater** than your current list price |

You may also **sell at any time** from the lives sheet (not only on a housing
tile). Sale pays current value, remaining mortgage is paid off from proceeds,
leftover cash is yours, the card returns to the pool, and you must immediately
pick a rental.

---

## Purchase: cash or mortgage

Both options are always offered for the chosen house.

| Path | What happens |
| --- | --- |
| **Cash** | Pay the full list price from the bank. The house is yours for the rest of the run unless you sell or move. No payday payments, no grace, no foreclosure. Total paid = **100%** of list |
| **Mortgage** | Pay **20% of list price** up front. That 20% is **interest** — it does **not** reduce the balance. The **full list price** is then split into **20 equal amounts**, due automatically from the bank the moment you **cross a payday tile**, until the entire table value is paid down. Total paid = **120%** of list |

Worked example (Ranch house, $260k):

- Cash: pay $260k once.
- Mortgage: $52k down (sunk, not principal). Balance stays **$260k**. $260k ÷ 20 = **$13k** taken on each of the next 20 payday crossings. Lifetime cost **$312k**.

The 20% is why cash is the economic play *if you can fund the whole sticker*. Financing is the liquidity play, and it costs you.

If cash is short of the down payment (or the cash price), that house cannot
be bought that way — pick the other path, a cheaper card, a rental, or take a
bank loan first.

**Estate Minded** (Brains +75 B) doubles appreciation while you own a house.
It does not change list price, down payment, or the 20-payment split.

### Missed payments and foreclosure

Payment is automatic. If the bank cannot cover it:

1. The missed amount stays as **arrears**.
2. You spend **one grace period** (you get **two** total on this mortgage).
3. The next payday tries to collect current payment **plus** arrears.

If a payment comes due with **both grace periods already used** and the bank
still cannot cover it, **foreclosure is automatic**:

- The house returns to the exclusive pool.
- Remaining mortgage is wiped (the bank takes the house). You do not keep
  equity.
- You must immediately pick a rental.

Grace periods reset if you pay the mortgage off, sell, or take a new mortgage
on a move.

### Selling

Allowed at any time. Price = **current value** (purchase price + appreciation
to date). Mortgage remainder (whatever of the **full list** is still unpaid)
comes out of the proceeds first. The 20% down is already gone — it was never
equity. Then you must choose a rental. You may buy again at a later housing
tile if you still own none.

Sell the ranch the day you close, value still $260k, remaining mortgage $260k:
proceeds wipe the loan, leftover **$0**. The $52k down is the interest you
paid to have been in the house at all.

### Moving

Only on a later housing tile, and only to a house with **greater list price**
than the one you have.

| | Rule |
| --- | --- |
| Draw | 3 remaining houses priced above your current list price |
| Move cost | Flat **$10k** from the bank (**Starter Home** waives this) |
| New mortgage | `remaining mortgage + (new list price − old list price)`. Then **reset** that balance across the **next 20 paydays**, payments recalculated. No second 20% interest fee — that fee is only on a financed purchase |
| Cash owners | Remaining mortgage is $0, so the value gap *becomes* the new 20-payment mortgage (face value, no extra 20%). Still pay the $10k |
| Perk | Old house perk ends. New house perk is revealed on purchase, still hidden at draw |
| Old card | Returns to the exclusive pool |

You cannot move *down* in list price on these tiles. To leave a house without
upgrading, sell and rent.

---

## Purchase options

Costs in the spreadsheet are thousands of dollars.

| id | name | price | perk (hidden until owned) |
| --- | --- | --- | --- |
| h-houseboat | Houseboat | $60k | Title: "First Mate [Name]". Visible to other players. No stat effects |
| h-container | Container Home | $60k | |
| h-rv | RV | $80k | Title: "Vanlife [Name]". Visible to other players. **+1 to this player's movement** while owned (does not change the shared market tick) |
| h-treehouse | Treehouse | $80k | +1 karma per paycheck while owned |
| h-trailer | Double-wide Trailer | $90k | |
| h-duplex | Suburban Duplex | $100k | |
| h-starter | Starter Home | $100k | Moving costs are waived |
| h-condo | Urban Condo | $120k | |
| h-sf3 | Single Family 3 Bedroom | $130k | |
| h-beach | Beach Hut | $140k | |
| h-loft | Urban Luxury Loft | $140k | Title: "[Name], The Gentrifier". Visible to other players. No stat effects |
| h-cabin | Log Cabin | $150k | +10 flat buff to Brawn |
| h-townhouse | Townhouse | $150k | |
| h-split | Split Level | $160k | |
| h-cottage | Countryside cottage | $180k | |
| h-brownstone | Brownstone | $200k | |
| h-colonial | Colonial | $200k | |
| h-chalet | Alpine Chalet | $225k | Title: "Monsieur [Name]" / "Mademoiselle [Name]". Visible to other players. No stat effects |
| h-farmhouse | Farmhouse | $240k | |
| h-ranch | Ranch house | $260k | |
| h-tudor | Tudor | $275k | |
| h-penthouse | Penthouse | $280k | Title: "[Name], the Playboy" / "[Name], the Playgirl". Visible to other players. No stat effects |
| h-lakehouse | Lakehouse | $300k | |
| h-contemporary | Contemporary Modern | $325k | |
| h-mcmansion | McMansion | $340k | |
| h-villa | Poolside Villa | $360k | |
| h-victorian | Victorian | $375k | Title: "Count [Name]". Visible to other players. No stat effects |
| h-castle | Scottish Castle | $450k | Title: "Lord [Name]". Visible to other players. No stat effects |
| h-mega | Mega Mansion | $600k | Title: "[Name], The Superior". Visible to other players. No stat effects |

29 cards. Draw-3 from this deck is plenty of variety. Titles are public (they
are the point); other perks stay off the HUD until you own the card.

Career discounts that mention "housing related payments" apply to mortgage
paydays, the cash purchase, the $10k move fee, and rental paydays — not to
appreciation.

---

## Rental options

Rent is charged automatically on every payday crossing, same hook as a
mortgage payment. No down payment, no equity, no appreciation, no
foreclosure. You may switch rentals only at a housing tile, after a sale, or
after foreclosure.

Perks (and the Studio child gate) are **hidden until chosen**, except the
Studio rule has to be enforced at pick time so a parent cannot land in it.

| id | name | rent / payday | perk (hidden until chosen) |
| --- | --- | --- | --- |
| r-basement | Parents Basement | $0 | 50-pt debuff to Buds: absolute value of Buds is reduced by 50, floored at 0 |
| r-motel | Motel Room | $10k | +5% chance of rolling a layoff while chosen |
| r-studio | Studio Apartment | $20k | Cannot be selected if the player has any children |
| r-hotel | Hotel Suite | $30k | 20-pt debuff to Brawn: absolute value of Brawn is reduced by 20, floored at 0 |
| r-house | Rental House | $40k | No debuff |

Absolute-value debuff means the stat is pulled **toward zero** (a +60 Buds
in the basement becomes +10; a −60 becomes −10). Floor 0: a +10 or −10
Basement tenant sits at 0 Buds from this effect.

If you are in a Studio and then have a child, you must immediately re-pick a
legal rental (or buy, if a housing tile is resolving).
