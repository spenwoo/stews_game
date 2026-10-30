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
must borrow from the bank at a cost and a decrease in karma. The rate of return
is randomized, to be determined.

### The problem: as written, investing is free money

If deposits are instant, returns are always positive, and the only withdrawal
cost is a turn, then the optimal play is trivially "deposit everything, always."
A mechanic with one correct answer isn't a decision — it's a tax on players who
forget to use it.

Two things make it a real choice:

**1. Returns must be able to lose money.**

**Proposal — roll per payday on the invested balance:**

| Roll | Return | |
| --- | --- | --- |
| 1 | −10% | Crash |
| 2 | −4% | Dip |
| 3 | +3% | Flat |
| 4 | +6% | Decent |
| 5 | +12% | Good |
| 6 | +22% | Boom |

Expected value **+4.8% per payday** — positive, so investing is correct *on
average*, with a 1-in-3 chance of losing money in any given window. Compounded
over 12 paydays an always-invested player roughly **1.75x**s their contributions,
but with wide variance.

**2. The one-turn withdrawal delay must bite.**

That delay is the actual cost of investing, and it's a good one: it creates
**liquidity risk**. You don't know what the next tile will demand. If you're
fully invested and land on a $40k loss, you can't reach your own money — you're
forced into a loan, paying interest and karma for the privilege of being
over-invested.

This turns "how much do I keep liquid?" into a live question every turn, which is
exactly what the interface should be for. It also interacts sharply with marriage,
since doubled involuntary costs mean a married player needs a bigger cash buffer.

**Undefined:** is the deposit also delayed, or instant? (Proposal: instant in,
delayed out — the asymmetry is what makes the trap work.) Can you withdraw
partially? (Proposal: yes, you name an amount and it arrives next turn.)

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
Net worth     = cash + investments + house sale value − (loans + interest)
Scoring tiers = max(0, positive tiers held − negative tiers held)

Final score   = Net worth × (1 + scoring tiers × 30%)
              + $150k per child
              + karma × $2k
              + career prestige bonus
```

Negative perks contribute **nothing** at scoring — their entire value was
realized during the run.

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

**Undefined:** does karma contribute to score at all, or is its only job the
mid-life crisis roll? The formula above assumes a modest $2k per point. See
[Q1 in doc 08](08-open-questions.md#q1--how-does-karma-work-as-a-separate-resource).
