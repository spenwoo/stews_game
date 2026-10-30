# 04 — Life Events

Life events are the structural beats of a run. All are mandatory stops
([doc 03](03-board-and-tiles.md#life-event-tiles)) so the shape of a game never
depends on a roll.

**Proposal — placement:**

| Event | Board position | Season |
| --- | --- | --- |
| University fork | Pre-board (tile 0) | — |
| Marriage | 20 | Fall |
| Buy a House | 28 | Fall |
| Children I | 34 | Fall/Winter |
| Children II | 44 | Winter |
| Mid-Life Crisis | 50 | Winter |
| Retirement | 72 | Spring |

Promotions and layoffs aren't tiles — they trigger at paydays.

---

## University

**Spec.** Two paths:

- **No school** — straight to career, limited career options.
- **Undergrad** — down the school track, costs funds, opens more career options.
  If undergrad is chosen, the player may then also choose **graduate school**,
  costing additional funds and opening enhanced versions of certain careers.

**Proposal — three resulting career tiers:**

| Path | Cost | Tiles spent | Career pool |
| --- | --- | --- | --- |
| No school | $0 | 0 | Tier 1 only |
| Undergrad | $80k (loan allowed) | 6 | Tiers 1–2 |
| Undergrad + grad | $160k total | 12 | Tiers 1–3 |

The trade is time and debt against earning ceiling. With 12 paydays in a game,
spending 12 tiles on grad school costs you roughly **2 paydays of income** on top
of the tuition, so the tier-3 salary premium has to be large enough to repay both
across the ~9 remaining paydays. That's a concrete balance equation to solve
rather than a guess — see
[doc 09, Finding 5](09-balance-model.md#finding-5--education-pays-by-about-the-right-amount).

Starting a game in debt is also the first real test of the loan system
([doc 05](05-economy-and-investments.md#loans)) — a no-school player starts clean
and liquid, which should feel like a genuine alternative strategy, not a
consolation prize.

## Careers

**Proposal — structure.** Each career has a tier (gated by education) and three
stages. Players draw a career from their eligible pool.

| Stage | Unlock | Salary |
| --- | --- | --- |
| Base | On draw | Career base |
| Senior | After 4 paydays in the career | ~1.5x base |
| Executive | After 8 paydays in the career | ~2.2x base |

Paydays counted **in the current career** — a layoff resets the counter, which is
what makes layoffs hurt beyond the salary cut.

Each career should also carry a small **perk** at Senior and Executive that isn't
money, so careers feel different from one another rather than being salary
numbers with job titles attached. Open: what those perks are, and how many careers
per tier. See [Q6 in doc 08](08-open-questions.md#q6--career-list-and-career-perks).

## Promotions and layoffs

**Spec.** Every career has Senior and Executive stages with higher salary and
better perks, unlockable after a certain number of paydays. At the same time,
there's a small chance at each paycheck of being laid off — chances affected by
charisma and intellect — and a laid-off player rerolls a new career path from the
base level.

**Proposal — layoff odds.** Checked once per payday:

```
chance = 5% − (Brains + Buds) / 40    [clamped to 0.5% … 12%]
```

| Brains + Buds | Chance per payday | Odds of ≥1 layoff over 12 paydays |
| --- | --- | --- |
| +200 (both maxed) | 0.5% | ~6% |
| 0 (neutral) | 5% | ~46% |
| −200 (both bottomed) | 10% | ~72% |

This gives the social and intellectual stats a clear, legible in-run job and
makes neutral play genuinely risky — a coin flip on getting laid off at least
once per game.

**The problem to solve.** Losing Executive stage and resetting to a base-tier job
on payday 9 is close to run-ending, which makes layoffs feel like punishment
rather than drama. Options worth weighing:

- Severance equal to 2 paydays of the lost salary.
- Reroll keeps your education tier (so a grad can't land a tier-1 job).
- The payday counter resets to 2 rather than 0, so re-promotion is faster.
- Executive stage is layoff-immune — you've made it.

See [Q7 in doc 08](08-open-questions.md#q7--how-punishing-should-a-layoff-be).

## Marriage

**Spec.** Players may choose to marry and pick a male or female partner. Married
players may choose an additional career for their spouse, at the same tier as
their own character, and earn **50% of that salary** while together. While
together, **any costs incurred to the player are doubled**. Non-married players
continue as normal.

**Settled: the rule stands as written — all costs double.** This looked like a
trap on paper (doubled outgoings seemed likely to swamp a half-salary), and
modelling says otherwise. Marriage comes out at **−4.3%** against staying
single — close enough to neutral that it's a real judgement call. Scoping the
doubling to only involuntary costs, which was the proposed fix, swings marriage
to **+22% and makes it an automatic take**. See
[doc 09, Finding 6](09-balance-model.md#finding-6--marriage-the-original-spec-was-right-my-proposal-was-wrong).

What the paper analysis missed is that a spouse's salary doesn't just offset
costs — it compounds, because the surplus flows into the investment account for
the rest of the game.

**The real cost of marriage is liquidity, not money.** Married players take
**$396k in loans versus $116k** for single players, more than triple. Doubled
involuntary costs mean you need a much larger cash buffer, so a married player
who invests aggressively gets squeezed into borrowing — which drains karma and
makes their mid-life crisis worse
([doc 05](05-economy-and-investments.md#loans)). That's the decision marriage
actually presents, and it's a good one.

**Settled — marriage is a life, not a toggle:**

| Feature | Rule |
| --- | --- |
| Wedding cost | One-time hit at the event, paid *before* doubling starts. Proposal: $15k |
| Spouse career | Same education tier, same career list |
| Spouse salary | +50% of spouse payday, while together |
| Costs | All costs double while together |
| Spouse promotions | Spouse payday-count tracks yours — they hit Senior/Exec when you do |
| Spouse layoffs | No. One layoff system is enough |
| Married-only tiles | Action/outcome cards tagged `married` can draw |
| Together at retirement | Flat score bonus if still married at the end |
| Divorce | Ongoing risk from low **Buds**, plus a face on the mid-life crisis deck |

Deferred (not v1): partner stat-lean, 4th family house card, anniversary stop.

### Divorce and Buds

**Settled.** Negative Buds quietly raises the chance the marriage ends. Positive
Buds makes it rare. You don't pick "get divorced" off a normal tile — it
creeps in through how you've been treating people.

**Proposal — checked once per payday while married**, same hook as layoffs:

```
chance = 2% − (Buds / 50)    [clamped to 0.5% … 18%]
```

| Buds | Per payday | Odds of ≥1 divorce over 10 paydays |
| --- | --- | --- |
| +100 | 0.5% | ~5% |
| 0 | 2% | ~18% |
| −25 | 2.5% | ~22% |
| −50 | 3% | ~26% |
| −100 | 4% | ~33% |

Wait — that curve is too flat on the negative side. Steeper proposal, the one
to tune against:

```
if Buds >= 0:  chance = 1% − Buds / 200          [floor 0.3%]
if Buds <  0:  chance = 1% + (|Buds| / 100) × 12% [ceil 13%]
```

| Buds | Per payday | Odds over 10 paydays |
| --- | --- | --- |
| +100 | 0.3% | ~3% |
| 0 | 1% | ~10% |
| −25 | 4% | ~34% |
| −50 | 7% | ~52% |
| −100 | 13% | ~75% |

A committed negative-Buds spouse is more likely than not to divorce before
retirement. A well-liked one almost never does. That's the implicit tax on
ghosting date night.

**On a `married` action tile, picking the bad option also rolls once** at the
current chance (in addition to the payday check). Flavor: the fight *is* the
risk.

When a divorce fires:

- Spouse salary stops. Costs un-double from the next tile on.
- One-time legal cost (proposal: $20k, *not* doubled — doubling just ended).
- Children stay. Upkeep continues. Parent tiles still draw.
- `married` tiles stop drawing. `divorced` tiles may (a small late-game slice).
- Together-at-retirement bonus is lost.
- Lives sheet shows divorced. Recap tells the lobby.

The mid-life crisis face `c-divorce` is a second, dramatic path — a forced
confrontation rather than a slow leak. Same aftermath.

## Buy a House

**Spec.** The player is offered a random selection of **3 potential houses** from
a larger deck.

**Proposal.** Each house card carries a purchase price and an end-game sale value
drawn from a range, so housing is a genuine investment decision with spread
rather than a fixed cost:

| Tier | Price | Sale value at retirement |
| --- | --- | --- |
| Starter | $120k | $100k – $180k |
| Mid | $250k | $200k – $380k |
| Premium | $450k | $350k – $700k |

Cheap houses are safe; expensive ones are leveraged bets that can outperform the
investment account or sink you. Since you only ever see 3 of the deck, your
housing options are a real constraint, not a menu.

**Undefined:** can you decline to buy entirely? Can you buy more than one house,
or upgrade later? Does a house carry ongoing cost?

## Children

**Spec.** Two separate events, each offering: **birth** (small money cost),
**adoption** (large money cost, gain of karma), or **no children** (continue).

**The gap.** As specified, children cost money and sometimes give karma, and
nothing else. Without a payoff they're a strictly bad financial choice, and with
"no children" always available, declining is always correct — so both events
become non-decisions.

**Settled — don't balance children on a single score number.** Married players
pay double, so no flat "$X per kid" is fair to both cases. Cash stays slightly
negative; value lives in content and late-game payoffs.

| Feature | When | Rule |
| --- | --- | --- |
| One-time cost | At the event | Birth cheap (~$10k), adoption expensive (~$40k) + karma. Doubled if married |
| Payday upkeep | Every payday after | ~$4k per child. **Doubled if married.** This is what makes one vs. two different |
| Parent-only tiles | Fall / winter / spring | Same hidden ±X action rule, plus some outcomes |
| College-for-kid | Optional stop after Children II | Pay a lot, gain karma + score. Can decline |
| Spring slice | Late board | Parents: grandkids, being looked after, empty nest. `no_children`: travel, mentoring, second act — declining is a path, not an empty skip |
| Legacy bonus | Retirement | Per child, scaled by karma and Buds — "how they turned out" |
| "Your kid became X" | Retirement recap | Flavor + small prestige, weighted by your stats |

The second children stop can still say no, even if the first said yes. Kids
survive a divorce; upkeep and parent tiles continue. Authoring notes:
[content/family.md](content/family.md).

## Mid-Life Crisis

**Spec.** Cannot be skipped. Roll one of the available mid-life crisis options
(to be decided). Outcomes are affected by accumulated karma.

**Proposal — starter deck.** Each crisis resolves on a karma check, with high
karma softening or inverting the outcome:

| Crisis | Low karma | High karma |
| --- | --- | --- |
| Buy the sports car | Large cost, Brains − | Same cost, resells well at retirement |
| Quit to chase a dream | Lose career, reroll tier 1 | Career change at same tier, Buds + |
| Health scare | Large cost, Brawn −− | Moderate cost, Brawn − |
| Reconnect with old friends | Cost, Buds + | Buds ++, unlocks a spring-season bonus |
| Back to school | Cost, lose 3 tiles of progress | Education tier +1 |
| Big move | Forced house sale at low end of range | House sells at high end |

This is the clearest single place where karma earns its keep: one unavoidable,
high-stakes moment where a whole game's worth of small moral choices cashes out.
Since karma sits outside the perk system
([doc 02](02-character-and-stats.md#karma)), this may end up being karma's *only*
decisive use — which is dramatic, but should be a deliberate choice. See
[Q1 in doc 08](08-open-questions.md#q1--how-does-karma-work-as-a-separate-resource).

Note the model found every archetype finishing around −10 karma, driven mostly by
loan penalties. If the crisis is karma-gated, karma needs enough positive sources
on action tiles that players can actually steer it.

## Retirement (tile 72)

**Proposal.** The board ends here and scoring resolves — houses sell,
investments liquidate, loans are called in, positive perk bonuses apply. See
[doc 05, Final Scoring](05-economy-and-investments.md#final-scoring).

**Undefined:** does the game end when the first player retires, or does everyone
finish? (Proposal: everyone finishes; retired players watch the summary while
others play out, as in the original.)
