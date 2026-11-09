# Outcome tiles

**List:** [tiles/outcomes.csv](tiles/outcomes.csv). **Map:** [tiles/board.md](tiles/board.md).
This page is the voice rules. New cards go in the CSV.

No choice. Land (or stop), read, apply, continue. These are the luck and the
pacing relief between decisions.

| Column | Meaning |
| --- | --- |
| id | Stable handle |
| season | summer / fall / winter / spring |
| money | Cash change |
| karma | Karma change |
| text | Player-facing one-liner |
| gates | blank or `married` / `parent` / `no_children` |
| tags | optional: `health` (ignored while **Roid Rage** is active) |
| notes | Design intent |

Use the money ladder: $0 / ±$2k / ±$5k / ±$10k / ±$25k / ±$40k. Karma in
small integers until Q1 locks a range — examples use ±3 to ±8.

Target: ~25 per season, ~100 total. Mix roughly half money-up, half money-down,
with karma riding on about a third of them.

---

## Summer

| id | money | karma | text | gates | notes |
| --- | --- | --- | --- | --- | --- |
| su-o01 | +2000 | 0 | Tax refund. You forgot you were owed this. | | |
| su-o02 | -2000 | 0 | Parking tickets you ignored caught up. | | |
| su-o03 | +5000 | 0 | Your old couch sold for more than it deserved. | | |
| su-o04 | 0 | +5 | You returned a wallet. They wrote you a note. | | Pure karma |
| su-o05 | -5000 | 0 | The used car needs a new transmission. Already. | | |
| su-o06 | +2000 | +3 | A friend covers dinner. You were going to. | | |
| su-o07 | -2000 | -3 | You "forget" to split the bill evenly. | | |
| su-o08 | 0 | -5 | You ghost a group project and it shows. | | |

*Queue — summer: 17 more to ~25.*

## Fall

| id | money | karma | text | gates | notes |
| --- | --- | --- | --- | --- | --- |
| fa-o01 | -10000 | 0 | HOA special assessment. Nobody is happy. | | |
| fa-o02 | +10000 | 0 | Side gig actually pays this month. | | |
| fa-o03 | -5000 | 0 | Wedding gift you can't really afford. | | Awkward if they skipped marriage |
| fa-o04 | +5000 | +3 | A relative leaves you a little something. | | |
| fa-o05 | 0 | +5 | You give a stranger a jump in the rain. | | |
| fa-o06 | -25000 | 0 | The roof. It's always the roof. | | |
| fa-o07 | +2000 | 0 | Credit-card points you actually redeem. | | |
| fa-o08 | -2000 | -3 | Impulse gadget. In a drawer by Friday. | | |

*Queue — fall: 17 more to ~25.*

## Winter

| id | money | karma | text | gates | notes |
| --- | --- | --- | --- | --- | --- |
| wi-o01 | -10000 | 0 | Dental work nobody budgeted for. | | health |
| wi-o02 | +25000 | 0 | Bonus year. Don't get used to it. | | |
| wi-o03 | -5000 | +8 | You cover a coworker's shortfall quietly. | | Money for karma |
| wi-o04 | 0 | -5 | You take credit for work that wasn't yours. | | |
| wi-o05 | -40000 | 0 | Family emergency travel. Last-minute fares. | | |
| wi-o06 | +5000 | 0 | Insurance actually covers it. Shocking. | | |
| wi-o07 | -2000 | 0 | Field trip money. Again. | parent | |
| wi-o08 | +2000 | +5 | The kid's lemonade stand, minus the sugar. | parent | |

*Queue — winter: 17 more to ~25.*

## Spring

| id | money | karma | text | gates | notes |
| --- | --- | --- | --- | --- | --- |
| sp-o01 | +10000 | 0 | A hobby turns into a little extra income. | | |
| sp-o02 | -10000 | 0 | You finally replace the thing you've been patching. | | |
| sp-o03 | 0 | +8 | You write the recommendation that gets them the job. | | |
| sp-o04 | +5000 | +3 | An old friend repays a loan you'd written off. | | |
| sp-o05 | -5000 | 0 | Reunion you said you'd skip. You don't skip it. | | |
| sp-o06 | 0 | +5 | You show up. That's the whole tile. | parent | |
| sp-o07 | +25000 | 0 | Downsizing sale. The attic was a gold mine. | | |
| sp-o08 | -25000 | +5 | You fund something that will outlast you. | | Legacy spend |

*Queue — spring: 17 more to ~25. Include `no_children` travel variants.*
