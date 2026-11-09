# 05 — Economy & Investments

## Money scale

**Proposal.** Real-feeling dollar amounts, because the game is about a life and
the numbers should read as recognizable. One payday ≈ several years of earnings
compressed, so salary figures are per-payday, not annual.

| | Value |
| --- | --- |
| Starting cash | $25,000 |
| Paydays per game | 12 |
| Typical outcome tile swing | ±$5k – $40k |
| Typical life event cost | $80k – $450k |

## Salary bands

**Proposal.** Narrow bands between tiers, deliberately — see the calculation
below for why.

| Tier | Education required | Base per payday |
| --- | --- | --- |
| 1 | None | $25k – $35k |
| 2 | Undergrad | $40k – $50k |
| 3 | Undergrad + grad | $55k – $70k |

With Senior at 1.5x and Executive at 2.2x
([doc 04](04-life-events.md#careers)), lifetime earnings for a mid-band career
that never gets laid off:

| Path | Paydays | Gross | Tuition | Net |
| --- | --- | --- | --- | --- |
| No school, tier 1 ($30k) | 12 | $526k | $0 | **$526k** |
| Undergrad, tier 2 ($45k) | 11 | $713k | $80k | **$633k** |
| Grad, tier 3 ($62k) | 10 | $892k | $160k | **$732k** |

That's a **~28% spread** from the cheapest to the most expensive path. The reason
to keep it that tight: education costs both money *and* paydays, so a wide salary
band compounds into a runaway. An earlier pass with tier 3 at ~$85k produced a
3x lifetime gap, which would make grad school mandatory and the education fork a
fake choice. At 28%, the no-school player starts debt-free and liquid two paydays
earlier, which is a real counter-strategy — they can be in the investment market
while the grad student is still paying tuition.

See [doc 09, Finding 5](09-balance-model.md#finding-5--education-pays-by-about-the-right-amount).

## Investments

**Spec.** A separate interface the player can open at any time. Money can be
moved from the bank into an investment account to earn a return. **Withdrawing
takes one turn.** If an action or outcome tile creates a shortfall, the player
must borrow from the bank at a cost and a decrease in karma.

**Settled — shared spin market.** Every spinner result in the lobby, from
*any* player, moves **every** invested balance by the same percentage. One
table, one tick, everyone rides it. Later, individual tiles will add one-off
market shocks on top of this weather. Returns are still **game-time** (spins),
never wall-clock.

### Per-spin table

Equal faces. **6+** is the boom bucket on this *market* die (a fair 1–6,
separate from movement modifiers).

| Spin | Effect | Odds |
| --- | --- | --- |
| 1 | −1.00% | 1/6 |
| 2 | −0.50% | 1/6 |
| 3 | 0.00% | 1/6 |
| 4 | +0.33% | 1/6 |
| 5 | +0.75% | 1/6 |
| 6+ | +1.25% | 1/6 |

Expected value **+0.138% per spin**. In a 6-player lobby that's **+0.83% per
round** (six ticks). 1-in-3 spins lose money; 1-in-2 make money; a 3 is flat.

### The problem: as written, investing is free money

If deposits are instant, returns are always positive, and the only withdrawal
cost is a turn, then the optimal play is trivially "deposit everything, always."
This table keeps a 1-in-3 chance of a down tick so the average is positive
without being free. The *decision* is still liquidity:

**The one-turn withdrawal delay must bite.** You don't know what the next tile
will demand. If you're fully invested and land on a $40k loss, you can't reach
your own money — you're forced into a loan. In a 6-player lobby that delay also
lets the other five players' spins tick your account before the cash arrives.

Deposit is instant; withdrawal is delayed; partial withdrawals allowed. That
asymmetry is the trap. Marriage makes it sharper (doubled involuntary costs →
bigger cash buffer).

Per-spin moves are small (−1% of $200k is $2k). **Crashes that feel like
crashes belong on tiles**, not on this weather table.

### Balance vs current salaries

Excel payday mids are roughly **$30k–$250k**. A mid career on 12 paydays
(4 / 4 / 4 at base / promo 1 / promo 2) lands around **$800k–$1.3M** gross
(Teacher $800k, Nurse $1.22M, Sales $1.30M, Investment Banker $2.04M). Starting
cash is $25k. Surplus into the market is a slice of that, not the whole paycheck
— mortgage, rent, kids, and the cash buffer eat first.

The **old** payday table (+4.8%/payday, ~1.75× over 12 paydays) was a second
career. This table is a kicker. Compounded, always-invested, no new deposits:

| Spins / player | Solo | 2p | 6p |
| --- | --- | --- | --- |
| ~22 (72-tile placeholder) | +3% | +6% | **+20%** |
| ~40 (modest long board) | +6% | +12% | **+39%** |
| ~60 (closer to 30 action landings at 1–6) | +9% | +18% | **+65%** |

A more realistic player who banks **20% of an $80k payday** ($16k × 12 = $192k
DCA) in a 6p game with ~2–3 spins between paydays finishes about **$22k–$35k
up** — a fraction of one paycheck. That is the right size: investing is
correct *on average*, it does not outrun salary, and the no-school liquidity
path is a real edge rather than a runaway.

**Mortgage-to-invest vs cash house** does **not** recoup the 20% interest on
this table except in a long 6p game with the float invested the whole remaining
board. A $260k ranch: $52k sunk interest vs ~$24k market profit on the $208k
float in a 6p / 22-spin game, ~$46k at 40 spins, ~$72k at 60. Cash is still
the economic house play if you can fund the sticker; mortgage is liquidity.

### What to watch

1. **Lobby size is a 6× multiplier, and that is accepted.** Same deposited
   dollar earns ~6× in a full lobby vs solo. 6p at +0.83%/round is the
   intended feel. Solo stays on the quieter per-spin curve — **no ghost
   rolls.**
2. **Movement perks do not pump the market.** The shared tick is always a
   fair **1–6**, once per player turn. **Daredevil**, **Speedster**,
   **Roid Rage** max+1, and the **RV** +1 change only that player's
   movement. Other portfolios are not biased by someone else's die.
3. **Board length still multiplies this.** Q4 (how we get ~30 action
   landings) decides whether 6p sits at +20% or +65% on money that was in
   from the start. DCA of late salary never gets the full duration, so the
   headline compound is an upper bound.
4. **Investment Banker** (+5% on gains and +5% on losses) is tiny on ±1%
   ticks. Leave it until tile shocks exist; those are where the perk will
   show.
5. **P(finish underwater)** if you never touch the account: ~19% after 22
   solo ticks, ~2% after 132 ticks (6p, short board), ~0% after a long 6p
   game. The weather table almost never sinks a 6p buy-and-hold. Downside
   lives in tile shocks and the loan you take when you're illiquid.

**Journey(wo)man** ($5k auto-deposit per paycheck) is flavor on this curve,
not a build.

## Loans

**Spec.** On a shortfall the player borrows from the bank at a cost and loses
karma.

**Proposal:**

| | Value |
| --- | --- |
| Interest | 20% flat on principal, due at retirement |
| Karma cost | −5 karma per loan taken |
| Trigger | Automatic on any shortfall; also voluntary |

Flat-rather-than-compounding keeps the math phone-friendly.

The karma hit is what makes borrowing more than an interest charge. With karma
as a separate resource, its main consumer is the mid-life crisis roll
([doc 04](04-life-events.md#mid-life-crisis)) — so a player who runs their
finances on the edge for the first half of the game arrives at tile 50 with
depleted karma and gets the worse outcome. That's a clean, legible consequence
chain: borrow often → bad crisis.

It also means karma needs enough other sources to stay a managed resource rather
than a loan counter. See
[Q1 in doc 08](08-open-questions.md#q1--how-does-karma-work-as-a-separate-resource).

Education debt uses the same system, which is why a grad-school start is also a
small karma start.

## Final Scoring

**Spec intent.** Positive perks unlock bonuses at the end of the game; negative
perks pay off during it. Solo mode is score-focused.

**Formula (modelled, see [doc 09](09-balance-model.md)):**

```
Net worth     = cash + investments + (house current value − remaining mortgage) − (loans + interest)

Final score   = Net worth
              + each *currently active* positive perk's retirement effect
              + family bonuses (together, child legacy, etc.)
              + karma × $1,000 (uncapped, hidden; Enlightened triples if active)
              + career prestige bonus
```

Negative perks contribute **nothing** at scoring — their entire value was
realized during the run. The old "30% per net tier" figure is now a **budget
for authoring** the two-choice positive perks, not a second hidden multiplier.
Don't stack both. List: [content/perks.md](content/perks.md).

### Why scoring is on *net* tiers

This is the single most important mechanical detail in the formula, and it isn't
obvious. Because every action tile option raises one stat while lowering another,
a player committed to the negative path **picks up positive tiers in their
off-stats by accident** — around 1.3 of them. If scoring counted every positive
tier held, negative builds would collect multipliers they never committed to, and
raising the positive multiplier to help positive builds would buff negative
builds too. The gap never closes: at a 50% per-tier multiplier the negative build
was *still* ahead.

Subtracting negative tiers first fixes it, and it's better design anyway — the
end-game bonus now rewards genuine commitment rather than drift. You can't hedge
your way into a multiplier. Full numbers in
[doc 09, Finding 3](09-balance-model.md#finding-3--positive-multipliers-leak-to-negative-builds).

### The two dials

**Negative perk value** (cash per payday per tier) and **positive multiplier**
(per net tier) have to be tuned against each other. Solved pairings:

| Negative perk value | Required positive multiplier |
| --- | --- |
| $6k | 15.6% |
| **$18k** | **29.6%** ← recommended |
| $30k | 40.7% |

At the recommended pairing, committed positive and committed negative builds
finish **level on average**, which is the target from
[doc 02](02-character-and-stats.md#the-intended-risk-curve).

One target is still missed: the negative build should be the *higher*-variance
option and currently isn't, because a flat per-payday payout is the most reliable
income in the game. **Negative perks should therefore be written as windfalls and
gambles, not as a stipend** — that's a content rule for perk authoring rather
than a number.

Karma is an uncapped hidden currency; the $1,000/pt line is the fog at
retirement. See [doc 12](12-karma-health-housing-start.md#1-karma).
