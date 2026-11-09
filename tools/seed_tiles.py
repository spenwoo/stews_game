"""Seed action and outcome CSVs. Run: py tools/seed_tiles.py"""

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TILES = ROOT / "docs" / "content" / "tiles"

ACTIONS = [
    # youth
    ("su-a01", "summer", "youth", "same", "brawn", "brawn", 10, "Train for a half marathon", "Snack time on the couch", -100, 0, "", "Canonical example"),
    ("su-a02", "summer", "youth", "same", "brains", "brains", 10, "Take the night class", "Binge the whole series", -2000, 0, "", "Good costs money"),
    ("su-a03", "summer", "youth", "same", "buds", "buds", 10, "Show up to your roommate's birthday", "Ghost the group chat", -50, 0, "", "Tiny cost, social"),
    ("su-a04", "summer", "youth", "split", "brains", "buds", 10, "Stay in and finish the certification", "Go out, you'll study tomorrow", 0, -40, "", "Split: future vs tonight"),
    ("su-a05", "summer", "youth", "split", "buds", "brawn", 10, "Help a friend move", "Sleep in, they have other friends", 0, 0, "", ""),
    ("su-a06", "summer", "youth", "same", "brawn", "brawn", 10, "Bike to work all month", "Lease the flashy compact", 0, -8000, "", "Bad costs — short-sighted spend"),
    ("su-a07", "summer", "youth", "split", "brains", "brawn", 10, "Cook actual dinners", "Takeout every night", -200, -1500, "", "Both cost; bad costs more"),
    ("su-a08", "summer", "youth", "same", "buds", "buds", 10, "Call your parents on Sunday", "Let it go to voicemail again", 0, 0, "", ""),
    # college — Brains-heavy
    ("co-a01", "summer", "college", "same", "brains", "brains", 10, "Live in the library the week before finals", "Cram off a roommate's notes in the hallway", 0, 0, "", "Brains focus"),
    ("co-a02", "summer", "college", "split", "brains", "buds", 10, "Skip the party, finish the paper", "The paper can be late", 0, -20, "", ""),
    ("co-a03", "summer", "college", "same", "brains", "brains", 10, "Office hours even though it's awkward", "Email the prof at 2am instead", 0, 0, "", ""),
    ("co-a04", "summer", "college", "split", "buds", "brains", 10, "Join the club that actually meets", "Pay dues and never go", -40, -40, "", "Same money"),
    # work — early cash / Brawn
    ("wk-a01", "summer", "work", "same", "brawn", "brawn", 10, "Take the extra closing shift", "Call in tired", 0, 0, "", "Early cash path"),
    ("wk-a02", "summer", "work", "split", "brawn", "brains", 10, "Learn the trade from the lifer on nights", "Watch tutorials and call it training", 0, 0, "", ""),
    ("wk-a03", "summer", "work", "same", "buds", "buds", 10, "Cover a coworker's shift, no questions", "Let them scramble", 0, 0, "", ""),
    ("wk-a04", "summer", "work", "split", "brains", "brawn", 10, "Put part of the check into a class", "Blow it on the weekend", -1500, -1500, "", ""),
    # grad — Brains
    ("gr-a01", "fall", "grad", "same", "brains", "brains", 10, "Rewrite the chapter that isn't working", "Submit it and hope the committee skims", 0, 0, "grad", "Brains focus"),
    ("gr-a02", "fall", "grad", "split", "brains", "brawn", 10, "Sleep after the lab, not in it", "Another all-nighter, you're fine", 0, 0, "grad", ""),
    ("gr-a03", "fall", "grad", "same", "brains", "brains", 10, "Go to the visiting lecture", "You already know this stuff", 0, 0, "grad", ""),
    ("gr-a04", "fall", "grad", "split", "buds", "brains", 10, "Help a first-year through quals", "Guard your notes", 0, 0, "grad", ""),
    # career track
    ("ct-a01", "fall", "career_track", "same", "brains", "brains", 10, "Volunteer to lead the messy project", "Let someone else take the heat", 0, 0, "", ""),
    ("ct-a02", "fall", "career_track", "split", "brains", "buds", 10, "Work the weekend to make Senior", "Protect Saturday for people", 0, 0, "", ""),
    ("ct-a03", "fall", "career_track", "same", "brawn", "brawn", 10, "Join the rec league", "Skip, your knees are fine", -200, 0, "", ""),
    ("ct-a04", "fall", "career_track", "split", "buds", "brains", 10, "Take the new hire to lunch", "Eat at your desk, you're busy", -40, 0, "", ""),
    # brawn gated
    ("br-a01", "fall", "brawn", "same", "brawn", "brawn", 10, "Train for the overnight hike", "Drive to the viewpoint and call it done", -80, 0, "", "Gate stat focus"),
    ("br-a02", "fall", "brawn", "same", "brawn", "brawn", 10, "Spot your friend through the last set", "Skip, they have a machine", 0, 0, "", ""),
    ("br-a03", "fall", "brawn", "split", "brawn", "brains", 10, "Protect your sleep", "Answer email at midnight", 0, 0, "", ""),
    ("br-a04", "fall", "brawn", "split", "brawn", "buds", 10, "Run the 10k you signed up for", "No-show and keep the shirt", -40, 0, "", ""),
    # open brawn — equal money, less Brawn targeting
    ("ob-a01", "fall", "open_brawn", "same", "buds", "buds", 10, "Host a small dinner anyway", "Make an excuse, order in alone", -1500, -80, "", ""),
    ("ob-a02", "fall", "open_brawn", "same", "brains", "brains", 10, "Read the whole contract", "Initial every page without looking", 0, 0, "", ""),
    ("ob-a03", "fall", "open_brawn", "split", "brains", "brawn", 10, "Stay late to understand the tool", "Have the intern do it", 0, 0, "", ""),
    ("ob-a04", "fall", "open_brawn", "split", "buds", "brawn", 10, "Walk the long way with them", "Drive, you're tired", 0, 0, "", ""),
    # lone — Buds-down path still uses good=+ Buds / bad=− Buds
    ("ln-a01", "fall", "lone", "same", "buds", "buds", 10, "Mute the group chat for a week, then come back", "Leave people on read for a month", 0, 0, "", "Negative-Buds route still offers the raise"),
    ("ln-a02", "fall", "lone", "split", "brains", "buds", 10, "Work from home and actually work", "Work from home and disappear", 0, 0, "", ""),
    ("ln-a03", "fall", "lone", "same", "buds", "buds", 10, "Send the one text you owe", "Let the birthday pass", 0, 0, "", ""),
    ("ln-a04", "fall", "lone", "split", "brawn", "buds", 10, "Go to the gym nobody talks at", "Skip because someone might say hi", 0, 0, "", ""),
    # open lone
    ("ol-a01", "fall", "open_lone", "same", "buds", "buds", 10, "Show up to the thing you RSVP'd", "Bail an hour before", 0, 0, "", ""),
    ("ol-a02", "fall", "open_lone", "split", "brains", "brawn", 10, "Cook actual dinners", "Takeout every night", -200, -1500, "", ""),
    ("ol-a03", "fall", "open_lone", "same", "brains", "brains", 10, "Do the continuing-ed module", "Click through on mute", -100, 0, "", ""),
    ("ol-a04", "fall", "open_lone", "split", "buds", "brains", 10, "Make the call", "Send a calendar invite instead", 0, 0, "", ""),
    # social — Buds +50
    ("so-a01", "winter", "social", "same", "buds", "buds", 10, "Host the reunion even though it's a lot", "Forward a group email and skip", -1500, 0, "", "Gate stat focus"),
    ("so-a02", "winter", "social", "same", "buds", "buds", 10, "Sit through the school play", "Catch up on work in the parking lot", 0, 0, "parent", ""),
    ("so-a03", "winter", "social", "split", "buds", "brains", 10, "Take a casserole to the neighbor", "Close the blinds", -30, 0, "", ""),
    ("so-a04", "winter", "social", "split", "buds", "brawn", 10, "Dance at the wedding", "Hold up the wall", 0, 0, "married", ""),
    # open social
    ("os-a01", "winter", "open_social", "same", "brawn", "brawn", 10, "Get the checkup you've been skipping", "You'll go next year", -800, 0, "", ""),
    ("os-a02", "winter", "open_social", "split", "brains", "brawn", 10, "Learn the new tool at work", "Have the intern do it", 0, 0, "", ""),
    ("os-a03", "winter", "open_social", "same", "brains", "brains", 10, "Refinance and actually read the terms", "Sign whatever they put in front of you", 0, 0, "", ""),
    ("os-a04", "winter", "open_social", "split", "brains", "buds", 10, "Help with homework even though you're fried", "Hand them a tablet", 0, 0, "parent", ""),
    # scholar — Brains +75
    ("sc-a01", "winter", "scholar", "same", "brains", "brains", 10, "Take the night seminar just to stay sharp", "You already peaked, skip it", -2000, 0, "", "Gate stat focus"),
    ("sc-a02", "winter", "scholar", "same", "brains", "brains", 10, "Write the thing you've been meaning to write", "Let the draft rot", 0, 0, "", ""),
    ("sc-a03", "winter", "scholar", "split", "brains", "buds", 10, "Quiet hours in the study", "The group wants a game night", 0, 0, "", ""),
    ("sc-a04", "winter", "scholar", "split", "brains", "brawn", 10, "Sleep, then the paper", "Another all-nighter", 0, 0, "", ""),
    # open scholar
    ("oh-a01", "winter", "open_scholar", "same", "buds", "buds", 10, "Visit your parents this month", "Send a check instead", -400, -400, "", ""),
    ("oh-a02", "winter", "open_scholar", "split", "brawn", "brains", 10, "Start physical therapy", "Push through, it'll loosen up", -1200, 0, "", ""),
    ("oh-a03", "winter", "open_scholar", "same", "buds", "buds", 10, "Make the trip to see them", "You'll go next spring", -2000, 0, "", ""),
    ("oh-a04", "winter", "open_scholar", "split", "brains", "buds", 10, "Mentor the kid who reminds you of you", "Keep your methods to yourself", 0, 0, "", ""),
    # spine
    ("fa-a02", "fall", "spine_fall_a", "same", "buds", "buds", 10, "Host Thanksgiving even though it's a lot", "Make an excuse, order in alone", -1500, -80, "", ""),
    ("fa-a07", "fall", "spine_fall_b", "same", "buds", "buds", 10, "Plan a real date night", "Fall asleep on the couch together", -120, 0, "married", "Gated"),
    ("sp-a03", "spring", "spine_spring_a", "same", "brawn", "brawn", 10, "Keep the morning walk", "The chair is right there", 0, 0, "", ""),
    ("sp-a01", "spring", "spine_spring_b", "same", "buds", "buds", 10, "Make the trip to see them", "You'll go next spring", -2000, 0, "", ""),
]

OUTCOMES = [
    ("su-o01", "summer", "youth", 2000, 0, "Tax refund. You forgot you were owed this.", "", "", ""),
    ("su-o02", "summer", "youth", -2000, 0, "Parking tickets you ignored caught up.", "", "", ""),
    ("su-o03", "summer", "youth", 5000, 0, "Your old couch sold for more than it deserved.", "", "", ""),
    ("su-o04", "summer", "youth", 0, 5, "You returned a wallet. They wrote you a note.", "", "", "Pure karma"),
    ("su-o05", "summer", "youth", -5000, 0, "The used car needs a new transmission. Already.", "", "", ""),
    ("su-o06", "summer", "youth", 2000, 3, "A friend covers dinner. You were going to.", "", "", ""),
    ("su-o07", "summer", "youth", -2000, -3, "You forget to split the bill evenly.", "", "", ""),
    ("su-o08", "summer", "youth", 0, -5, "You ghost a group project and it shows.", "", "", ""),
    ("co-o01", "summer", "college", -10000, 0, "Lab fees nobody put in the brochure.", "", "", "Tuition flavor"),
    ("co-o02", "summer", "college", 2000, 3, "You find a scholarship you actually qualify for.", "", "", ""),
    ("co-o03", "summer", "college", -2000, 0, "The campus meal plan does not include dignity.", "", "", ""),
    ("wk-o01", "summer", "work", 5000, 0, "Overtime hits the account. You feel it in your back.", "", "", "Early cash"),
    ("wk-o02", "summer", "work", 2000, 0, "Tips were good. The night was long.", "", "", ""),
    ("wk-o03", "summer", "work", -2000, 0, "You needed new boots for the job. Already.", "", "", ""),
    ("gr-o01", "fall", "grad", -10000, 0, "Conference you had to attend. Out of pocket.", "", "grad", ""),
    ("gr-o02", "fall", "grad", 5000, 3, "A grant comes through. Small, but it comes through.", "", "grad", ""),
    ("gr-o03", "fall", "grad", 0, 5, "Your name is on the paper. You actually wrote it.", "", "grad", ""),
    ("ct-o01", "fall", "career_track", 10000, 0, "Side gig actually pays this month.", "", "", ""),
    ("ct-o02", "fall", "career_track", -5000, 0, "Work trip you fronted. Reimbursement pending.", "", "", ""),
    ("ct-o03", "fall", "career_track", 2000, 0, "Credit-card points you actually redeem.", "", "", ""),
    ("br-o01", "fall", "brawn", -2000, 0, "Physical therapy copay. You knew it was coming.", "", "health", ""),
    ("br-o02", "fall", "brawn", 2000, 0, "You sold the old bike for more than it was worth.", "", "", ""),
    ("ob-o01", "fall", "open_brawn", -10000, 0, "HOA special assessment. Nobody is happy.", "", "", ""),
    ("ob-o02", "fall", "open_brawn", 5000, 3, "A relative leaves you a little something.", "", "", ""),
    ("ln-o01", "fall", "lone", 0, -5, "You skip the thing. They notice.", "", "", ""),
    ("ln-o02", "fall", "lone", 5000, 0, "You didn't go out. The money is still there.", "", "", "Cash for isolation"),
    ("ol-o01", "fall", "open_lone", -2000, -3, "Impulse gadget. In a drawer by Friday.", "", "", ""),
    ("ol-o02", "fall", "open_lone", 0, 5, "You give a stranger a jump in the rain.", "", "", ""),
    ("so-o01", "winter", "social", -5000, 5, "You cover a friend's shortfall quietly.", "", "", "Money for karma"),
    ("so-o02", "winter", "social", 2000, 5, "The kid's lemonade stand, minus the sugar.", "", "parent", ""),
    ("os-o01", "winter", "open_social", -10000, 0, "Dental work nobody budgeted for.", "", "health", ""),
    ("os-o02", "winter", "open_social", 25000, 0, "Bonus year. Don't get used to it.", "", "", ""),
    ("sc-o01", "winter", "scholar", 0, 8, "You write the recommendation that gets them the job.", "", "", ""),
    ("sc-o02", "winter", "scholar", -2000, 0, "Another book. You already had two copies.", "", "", ""),
    ("oh-o01", "winter", "open_scholar", -40000, 0, "Family emergency travel. Last-minute fares.", "", "", ""),
    ("oh-o02", "winter", "open_scholar", 5000, 0, "Insurance actually covers it. Shocking.", "", "", ""),
    ("wi-o07", "winter", "spine_winter_c", -2000, 0, "Field trip money. Again.", "parent", "", ""),
    ("sp-o01", "spring", "spine_spring_a", 10000, 0, "A hobby turns into a little extra income.", "", "", ""),
    ("sp-o02", "spring", "spine_spring_a", -10000, 0, "You finally replace the thing you've been patching.", "", "", ""),
    ("sp-o07", "spring", "spine_spring_b", 25000, 0, "Downsizing sale. The attic was a gold mine.", "", "", ""),
]

ACTION_FIELDS = "id,season,branch,pair,good_stat,bad_stat,X,good,bad,good_money,bad_money,gates,notes".split(",")
OUTCOME_FIELDS = "id,season,branch,money,karma,text,gates,tags,notes".split(",")


def write(name, fields, rows):
    path = TILES / name
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for row in rows:
            w.writerow(dict(zip(fields, row)))
    print(name, len(rows))


def main():
    TILES.mkdir(parents=True, exist_ok=True)
    write("actions.csv", ACTION_FIELDS, ACTIONS)
    write("outcomes.csv", OUTCOME_FIELDS, OUTCOMES)


if __name__ == "__main__":
    main()
