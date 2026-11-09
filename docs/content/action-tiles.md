# Action tiles

**List:** [tiles/actions.csv](tiles/actions.csv). **Map:** [tiles/board.md](tiles/board.md).
This page is the voice rules. New cards go in the CSV.

**Format.** Player sees `prompt`, `good`, `bad`. After they pick, reveal
`stat` and `±X`. Money applies immediately if present.

| Column | Meaning |
| --- | --- |
| id | Stable handle, never reuse |
| season | summer / fall / winter / spring |
| pair | `same` (both options hit one stat) or `split` (good hits A, bad hits B) |
| good_stat | Stat the good option raises |
| bad_stat | Stat the bad option lowers |
| X | Magnitude, default 10 |
| good | Player-facing virtuous / effortful option |
| bad | Player-facing lazy / selfish / short-sighted option |
| good_$ | Cash change if they pick good (negative = cost) |
| bad_$ | Cash change if they pick bad |
| gates | blank, `married`, `parent`, `no_children`, `grad` |
| notes | Design intent, not player-facing |

Hidden from the player until after the choice: both stats, both signs, both
amounts. They can infer from flavor over time. Do not invert good/bad.

Target: ~40 per season, ~160 total. Examples below lock the voice — blank
rows are the queue.

---

## Summer — youth, first job

| id | pair | good_stat | bad_stat | X | good | bad | good_$ | bad_$ | gates | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| su-a01 | same | brawn | brawn | 10 | Train for a half marathon | Snack time on the couch | -100 | 0 | | Canonical example |
| su-a02 | same | brains | brains | 10 | Take the night class | Binge the whole series | -2000 | 0 | | Good costs money |
| su-a03 | same | buds | buds | 10 | Show up to your roommate's birthday | Ghost the group chat | -50 | 0 | | Tiny cost, social |
| su-a04 | split | brains | buds | 10 | Stay in and finish the certification | Go out, you'll study tomorrow | 0 | -40 | | Split: future vs. tonight |
| su-a05 | split | buds | brawn | 10 | Help a friend move | Sleep in, they have other friends | 0 | 0 | | |
| su-a06 | same | brawn | brawn | 10 | Bike to work all month | Lease the flashy compact | 0 | -8000 | | Bad *costs* here — exception, "short-sighted spend" |
| su-a07 | split | brains | brawn | 10 | Cook actual dinners | Takeout every night | -200 | -1500 | | Both cost; bad costs more |
| su-a08 | same | buds | buds | 10 | Call your parents on Sunday | Let it go to voicemail again | 0 | 0 | | |

*Queue — summer: 32 more to ~40.*

## Fall — building a life

| id | pair | good_stat | bad_stat | X | good | bad | good_$ | bad_$ | gates | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| fa-a01 | same | brains | brains | 10 | Volunteer to lead the messy project | Let someone else take the heat | 0 | 0 | | Career flavor |
| fa-a02 | same | buds | buds | 10 | Host Thanksgiving even though it's a lot | Make an excuse, order in alone | -1500 | -80 | | |
| fa-a03 | split | brawn | brains | 10 | Protect your sleep | Answer email at midnight | 0 | 0 | | |
| fa-a04 | same | brawn | brawn | 10 | Join the rec league | Skip, your knees are fine | -200 | 0 | | |
| fa-a05 | split | buds | brains | 10 | Take the new hire to lunch | Eat at your desk, you're busy | -40 | 0 | | |
| fa-a06 | same | brains | brains | 10 | Read the whole contract | Initial every page without looking | 0 | 0 | | |
| fa-a07 | same | buds | buds | 10 | Plan a real date night | Fall asleep on the couch together | -120 | 0 | married | Gated |
| fa-a08 | split | brains | buds | 10 | Work the weekend to make Senior | Protect Saturday for people | 0 | 0 | | Promotion temptation |

*Queue — fall: 32 more to ~40. Include ~6 `married`.*

## Winter — midlife

| id | pair | good_stat | bad_stat | X | good | bad | good_$ | bad_$ | gates | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| wi-a01 | same | brawn | brawn | 10 | Get the checkup you've been skipping | You'll go next year | -800 | 0 | | Health |
| wi-a02 | same | buds | buds | 10 | Sit through the school play | Catch up on work in the parking lot | 0 | 0 | parent | Gated |
| wi-a03 | split | brains | brawn | 10 | Learn the new tool at work | Have the intern do it | 0 | 0 | | |
| wi-a04 | same | buds | buds | 10 | Take a casserole to the neighbor | Close the blinds | -30 | 0 | | |
| wi-a05 | split | buds | brains | 10 | Visit your parents this month | Send a check instead | -400 | -400 | | Same money, different stat |
| wi-a06 | same | brains | brains | 10 | Refinance and actually read the terms | Sign whatever they put in front of you | 0 | 0 | | |
| wi-a07 | same | brawn | brawn | 10 | Start physical therapy | Push through, it'll loosen up | -1200 | 0 | | |
| wi-a08 | split | brains | buds | 10 | Help with homework even though you're fried | Hand them a tablet | 0 | 0 | parent | |

*Queue — winter: 32 more to ~40. Include ~8 `parent`.*

## Spring — late career, retirement approaching

| id | pair | good_stat | bad_stat | X | good | bad | good_$ | bad_$ | gates | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sp-a01 | same | buds | buds | 10 | Make the trip to see them | You'll go next spring | -2000 | 0 | | |
| sp-a02 | split | brains | buds | 10 | Mentor the kid who reminds you of you | Keep your methods to yourself | 0 | 0 | | |
| sp-a03 | same | brawn | brawn | 10 | Keep the morning walk | The chair is right there | 0 | 0 | | |
| sp-a04 | same | buds | buds | 10 | Tell them you're proud | They know, you don't have to say it | 0 | 0 | parent | |
| sp-a05 | split | buds | brains | 10 | Forgive the old grudge | Draft the letter you won't send | 0 | 0 | | |
| sp-a06 | same | brains | brains | 10 | Get the estate paperwork done | It'll sort itself out | -500 | 0 | | |
| sp-a07 | same | buds | buds | 10 | Take the grandkids for the weekend | You've done your time | -150 | 0 | parent | |
| sp-a08 | split | brains | brawn | 10 | Learn something with no career use | You've learned enough | -80 | 0 | | |

*Queue — spring: 32 more to ~40. Include parent, `no_children` travel/mentor variants.*
