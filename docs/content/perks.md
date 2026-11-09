# Perks

Copied from `data_files/Life Data File.xlsx` (Perks sheet). That folder is
user-owned — this file is the working copy.

Three stats × two directions × four thresholds × **two choices** = **48 perks**.
You pick one of the two when you first cross that threshold. Earlier picks
never lock later ones. Only perks whose threshold you *currently* hold are
active.

| Rule | |
| --- | --- |
| Voice | One sentence. One effect |
| Pairing | Two shapes at the same threshold |
| Scoring | These effects *are* the payout. Do not also apply a hidden 30% per-tier multiplier on top |
| In-run vs retirement | Mixed on both trees. The sheet is the source, not "positives retire / negatives swing" |

Numbers are starting points. Status `draft` until names are locked in playtests.

---

## How a pick works

Example: Brains hits +25. You choose **Collegiate** or **Prudent**. That choice
is remembered for the rest of the run.

- At Brains **+40** you have the +25 pick **on**. The +50 pick is not available.
- At Brains **+50** you choose again (Brilliant or Specialist), independent
  of the +25 pick. Now both are on.
- If Brains falls to **+40**, the +50 perk **turns off**. You cannot use it.
  The +25 perk stays on. The +50 *choice* is remembered, so if you climb back
  you do not re-pick.
- Crossing +25 the other way (down through zero into negatives) is a different
  tree. You can hold positive and negative perks on *different* stats at once,
  but one stat cannot be both +50 and −50.

Going negative on Buds still feeds divorce chance
([family.md](family.md#divorce--buds-is-the-leak)).

---

## Brains — intellect

### Positive

| Threshold | Pick | Name | Effect |
| --- | --- | --- | --- |
| +25 | A | **Collegiate** | Tier 1 schools become slightly more likely to be drawn when attending college |
| +25 | B | **Prudent** | Loan interest from attending college is reduced by 25% |
| +50 | A | **Brilliant** | +10% added to final net worth at retirement |
| +50 | B | **Specialist** | +$100k if you never took a layoff this run |
| +75 | A | **Accredited** | Awards a graduate degree: choose from three randomly chosen grad schools. One-time cost of $20k. No effect if you already have a graduate degree, or if you are missing an undergraduate degree |
| +75 | B | **Estate Minded** | House value appreciates 2× as much as normal |
| +100 | A | **Luminary** | Title of Professor Emeritus on the recap (visible to other players). +5 karma per paycheck in addition to all normal salary payments |
| +100 | B | **Enlightened** | Karma scores at 3× (helps or hurts, depending on the sign) |

### Negative

| Threshold | Pick | Name | Effect |
| --- | --- | --- | --- |
| −25 | A | **Imposter** | For initial career selection only, chance to roll from any career without needing college or grad school. +10% chance of being fired, for any career held while this perk is active |
| −25 | B | **Crammer** | Once per paycheck, skip the cash cost of a *good* action (stat still goes up) |
| −50 | A | **Manipulator** | Once per paycheck, skip the cash cost of any action tile |
| −50 | B | **Covert Intelligence** | All action tiles reveal their stat and sign *before* you pick |
| −75 | A | **Ignorant** | +$10k per paycheck as long as you have no current health ailment. Chance of rolling a health ailment +10% while this perk is active |
| −75 | B | **Inside Track** | Next promotion arrives 2 paydays early |
| −100 | A | **Pretender** | Switch careers with one player. All promotions are reset for both players |
| −100 | B | **Nepo Baby** | Once: dump your current career back into the exclusive pool, draw **3** remaining eligible careers, pick one, enter it already **Senior**. Old job is available to others again |

---

## Brawn — toughness

### Positive

| Threshold | Pick | Name | Effect |
| --- | --- | --- | --- |
| +25 | A | **Speedster** | In-run. Your spinner includes **7** as well as 1–6. Higher average movement — you get ahead, and you skip more tiles |
| +25 | B | **Well Rested** | Retirement: +$2k for every spin you made this run |
| +50 | A | **Athlete** | $5k from the bank anytime you roll a 6 or higher |
| +50 | B | **Team Player** | $1k from the bank anytime *any* player rolls a 6 or higher, paid to both you and the player who rolled |
| +75 | A | **Iron(wo)man** | Earn $5k from the bank any time you pass another player |
| +75 | B | **Journey(wo)man** | Every paycheck automatically deposits $5k into your investment account |
| +100 | A | **Unbreakable** | Can no longer be fired from any job |
| +100 | B | **Lifer** | One-time immunity to a health-ailment chance. Activates automatically and notifies you when used |

### Negative

| Threshold | Pick | Name | Effect |
| --- | --- | --- | --- |
| −25 | A | **Daredevil** | Your next 3 turns, **your** spinner is **1, 2, 5, 6, 7, 8** (no 3 or 4). Movement only — does not change the shared market tick. High ceiling (skip a lot) or crawl (land a lot) |
| −25 | B | **Bully** | Whenever a player within 10 tiles of you is **paid money**, take **$500** from them. No uses cap. Recap names it. If they have under $500 cash, take what they have — never loans them. Solo: no one to bully, perk is idle |
| −50 | A | **Second Chancer** | Once: after you see the tile you landed on, you may **re-spin**. The new result cannot be the same tile — if it would be, spin again until it isn't |
| −50 | B | **Line Cutter** | Switch tile spaces with any player of your choosing. Milestones the arriving player passes are assumed by them. Moving backwards lets that player re-choose when the milestone is reached again |
| −75 | A | **Welfare Queen/King** | If laid off, take severance equal to **4** paydays of the lost salary. Name follows character body (Queen / King) |
| −75 | B | **Thick Skin** | You may ignore the cash cost of the mid-life crisis; you still take the stat hit |
| −100 | A | **Sickly** | Health ailment passes from you to one opposing player of your choosing. One time. No notifications for other players; the ailment appears as if it happened naturally |
| −100 | B | **Roid Rage** | Instantly cure any current **health** problems, and ignore future ones while this perk is active. Max spinner roll +1. Layoff chance +5% |

---

## Buds — friendship

### Positive

| Threshold | Pick | Name | Effect |
| --- | --- | --- | --- |
| +25 | A | **Respected** | Retirement: +$40k "people showed up" |
| +25 | B | **Well Liked** | Retirement: +$1k per karma point accumulated |
| +50 | A | **Networker** | Whenever you are within 10 tiles of another player, any cash cost for action or outcome tiles is shared. Cost is divided by the number of players in range; each pays equally (rounded down to the nearest $100) |
| +50 | B | **Welcomer** | In-run. Whenever you are within 10 tiles of someone collecting a **payday**, you get **10% of that payday** from the **bank** (they keep their full pay). Solo: no nearby paydays, perk is idle — or treat as **Circle** (+together-bonus doubled, or +$50k if single) |
| +75 | A | **Expert Parent** | +5 karma awarded per child at retirement |
| +75 | B | **Problem Solver** | Rejects a divorce roll. Single use, activates automatically, notifies you when used |
| +100 | A | **Family Man/Woman** | Retirement: child legacy bonus counts 2× |
| +100 | B | **Keeper** | Retirement: +$150k if still married by retirement |

### Negative

| Threshold | Pick | Name | Effect |
| --- | --- | --- | --- |
| −25 | A | **Flake** | Once per game, decline a money-loss outcome as if you weren't there |
| −25 | B | **Joker** | The next time a `married` bad-option would roll extra divorce, it doesn't |
| −50 | A | **Mooch** | Next two money-loss outcomes are halved; −3 karma each time |
| −50 | B | **Smoker** | Once: a cost is "covered by someone." You don't pay. −10 karma. Recap names it; no other player is charged |
| −75 | A | **Inside Trader** | Investment withdrawals resolve this turn, not next (liquidity cheat) |
| −75 | B | **Grifter** | Choose one player and for the next three turns, trade salaries. Range not required. The other player is notified |
| −100 | A | **Gambler** | All remaining money outcomes swing an extra ±50% |
| −100 | B | **Midnight Toker** | If you divorce, waive the legal cost and take $80k "clean break" instead of the together-bonus |

---

## Design notes

- **48 to author, 4 active per fully-maxed stat-direction.**
- **Re-pick is off.** Remembered choices keep async turns short.
- **Enlightened** is the only positive perk that can *hurt* you (karma ×3).
- **Estate Minded** doubles the payday appreciation roll on a house you own,
  including dips. See [houses.md](houses.md).
- **Collegiate** weights PUB1 / PR1 draws at the University STOP.
  [schools.md](schools.md).
- **Nepo Baby** respects the exclusive career pool — the 3 you draw are from
  what's left, and your old job goes back in.
- **Pretender** swaps titles and resets both payday-in-job counters.
- **Line Cutter** can hand someone a STOP they already resolved, or send
  them back through one. The arriving player is the one who "passed" it.
- **Bully at $500 / Brawn −25** is frequent and now large enough to feel.
  Solo: idle.
- **Roid Rage "health problems"** means: chronic joint pain, cancer,
  Alzheimer's, and the mid-life health scare. Clears current, blocks new
  rolls while active, restores action choices if Alzheimer's was on.
- **Lifer** is the one-shot health dodge on the positive tree. **Ignorant**
  is the opposite tax: extra cash while healthy, extra ailment chance.
- **Spinner stacking.** Base 1–6. Speedster adds 7. Roid Rage raises the
  max face by 1 (6→7, or 7→8 if Speedster is also on). Daredevil, for three
  turns, *replaces* **your** movement die with {1,2,5,6,7,8} rather than
  adding to it. **RV** adds +1 to **your** movement while owned. None of
  these change the shared investment/housing tick (always a fair 1–6).
- **Proximity (10 tiles):** Welcomer, Bully, Networker, and Team Player
  (the last is lobby-wide on 6+ rolls, not range-gated).
- Power bands still sit near the old "30% per net tier" *budget*, but several
  positive perks now pay during the run.

## Still to confirm

- [ ] Names — keep, swap, or replace
- [ ] Welcomer solo fallback: idle, or Circle?
- [ ] Nepo Baby: once ever, or once per time you hold −100?
- [ ] Imposter: what "a chance to roll from any career" means as a number
- [ ] Accredited: does the $20k replace normal grad tuition, or sit on top?
