"""Generate docs/content/tiles/board-slots.csv from the map sketch.

Run: py tools/gen_board_slots.py
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "content" / "tiles" / "board-slots.csv"

TYPE = {"A": "action", "O": "outcome", "P": "payday"}


def mix(n: int, p: int = 0) -> list[str]:
    """n tiles, p of them payday; remaining split ~half action / half outcome."""
    assert 0 <= p <= n
    rest = n - p
    n_a = (rest + 1) // 2
    n_o = rest - n_a
    seq: list[str] = []
    a = o = 0
    while a < n_a or o < n_o:
        if a < n_a and (o >= n_o or a <= o):
            seq.append("A")
            a += 1
        else:
            seq.append("O")
            o += 1
    for i in range(p):
        pos = int((i + 1) * (len(seq) + 1) / (p + 1))
        seq.insert(min(pos, len(seq)), "P")
    assert len(seq) == n, (n, "".join(seq), len(seq))
    return seq


def rows_for_strip(region, branch, pattern, season, gate=""):
    rows = []
    for i, ch in enumerate(pattern, 1):
        rows.append(
            {
                "slot_id": f"{branch}-{i:02d}",
                "region": region,
                "branch": branch,
                "seq": i,
                "type": TYPE[ch],
                "season": season,
                "draw_pool": branch,
                "stop_event": "",
                "gate": gate,
                "notes": "",
            }
        )
    return rows


def stop(slot_id, region, event, season, notes=""):
    return {
        "slot_id": slot_id,
        "region": region,
        "branch": "spine",
        "seq": 0,
        "type": "stop",
        "season": season,
        "draw_pool": "",
        "stop_event": event,
        "gate": "",
        "notes": notes,
    }


def fork_tile(slot_id, region, event, season, notes):
    return {
        "slot_id": slot_id,
        "region": region,
        "branch": "spine",
        "seq": 0,
        "type": "fork",
        "season": season,
        "draw_pool": "",
        "stop_event": event,
        "gate": "",
        "notes": notes,
    }


def main():
    youth = mix(19)
    edu = mix(18)  # no payday — career has not started
    grad = mix(9)
    brawn = mix(16)
    lone = mix(16)  # Buds <= -25, early (after marriage)
    scholar = mix(16)  # Brains >= +75, after Children I
    social = mix(14)

    # 12 paydays on post-career *spine* only, so forks don't change salary count.
    to_marriage = mix(36, 2)
    to_house1 = mix(25, 1)
    to_brawn = mix(8, 0)
    to_child1 = mix(31, 2)
    to_house2 = mix(13, 1)
    to_child2 = mix(15, 1)
    to_house3 = mix(11, 0)
    to_social = mix(9, 0)
    to_child3 = mix(26, 1)
    to_midlife = mix(12, 1)
    to_house4 = mix(20, 1)
    to_retire = mix(38, 2)

    rows = []
    rows.append(stop("start", "youth", "start", "summer", "Character is on the board"))
    rows.extend(rows_for_strip("youth", "youth", youth, "summer"))
    rows.append(fork_tile(
        "uni", "university", "university", "summer",
        "STOP. Choose college or no-school, then enter fork_edu",
    ))
    rows.extend(rows_for_strip("fork_edu", "college", edu, "summer", "chose_college"))
    rows.extend(rows_for_strip("fork_edu", "work", edu, "summer", "chose_nocollege"))
    rows.append(fork_tile(
        "career", "career", "career", "fall",
        "STOP. Draw career. If undergrad, may take grad; else career_track",
    ))
    rows.extend(rows_for_strip("fork_grad", "grad", grad, "fall", "has_undergrad"))
    rows.extend(rows_for_strip("fork_grad", "career_track", grad, "fall", "none"))
    rows.extend(rows_for_strip("spine_to_marriage", "spine_to_marriage", to_marriage, "fall"))
    rows.append(stop("marriage", "marriage", "marriage", "fall"))
    rows.append(fork_tile(
        "fork-lone", "fork_lone", "fork_lone", "fall",
        "If Buds <= -25, choose lone or open_lone; else open_lone",
    ))
    rows.extend(rows_for_strip("fork_lone", "lone", lone, "fall", "buds_lte_neg25"))
    rows.extend(rows_for_strip("fork_lone", "open_lone", lone, "fall", "none"))
    rows.extend(rows_for_strip("spine_to_house1", "spine_to_house1", to_house1, "fall"))
    rows.append(stop("house1", "house", "house_1", "fall", "First buy / rent"))
    rows.extend(rows_for_strip("spine_to_brawn", "spine_to_brawn", to_brawn, "fall"))
    rows.append(fork_tile(
        "fork-brawn", "fork_brawn", "fork_brawn", "fall",
        "If Brawn >= +25, choose brawn or open_brawn; else open_brawn",
    ))
    rows.extend(rows_for_strip("fork_brawn", "brawn", brawn, "fall", "brawn_gte_25"))
    rows.extend(rows_for_strip("fork_brawn", "open_brawn", brawn, "fall", "none"))
    rows.extend(rows_for_strip("spine_to_child1", "spine_to_child1", to_child1, "winter"))
    rows.append(stop("child1", "children", "children_1", "winter", "Moved up — first children event"))
    rows.append(fork_tile(
        "fork-scholar", "fork_scholar", "fork_scholar", "winter",
        "If Brains >= +75, choose scholar or open_scholar; else open_scholar",
    ))
    rows.extend(rows_for_strip("fork_scholar", "scholar", scholar, "winter", "brains_gte_75"))
    rows.extend(rows_for_strip("fork_scholar", "open_scholar", scholar, "winter", "none"))
    rows.extend(rows_for_strip("spine_to_house2", "spine_to_house2", to_house2, "winter"))
    rows.append(stop("house2", "house", "house_2", "winter", "Buy if none / move if owned"))
    rows.extend(rows_for_strip("spine_to_child2", "spine_to_child2", to_child2, "winter"))
    rows.append(stop("child2", "children", "children_2", "winter"))
    rows.extend(rows_for_strip("spine_to_house3", "spine_to_house3", to_house3, "winter"))
    rows.append(stop("house3", "house", "house_3", "winter", "Buy if none / move if owned"))
    rows.extend(rows_for_strip("spine_to_social", "spine_to_social", to_social, "winter"))
    rows.append(fork_tile(
        "fork-social", "fork_social", "fork_social", "winter",
        "If Buds >= +50, choose social or open_social; else open_social",
    ))
    rows.extend(rows_for_strip("fork_social", "social", social, "winter", "buds_gte_50"))
    rows.extend(rows_for_strip("fork_social", "open_social", social, "winter", "none"))
    rows.extend(rows_for_strip("spine_to_child3", "spine_to_child3", to_child3, "winter"))
    rows.append(stop("child3", "children", "children_3", "winter", "Third children event"))
    rows.extend(rows_for_strip("spine_to_midlife", "spine_to_midlife", to_midlife, "winter"))
    rows.append(stop("midlife", "midlife", "midlife", "winter"))
    rows.extend(rows_for_strip("spine_to_house4", "spine_to_house4", to_house4, "spring"))
    rows.append(stop("house4", "house", "house_4", "spring", "Buy if none / move if owned"))
    rows.extend(rows_for_strip("spine_to_retire", "spine_to_retire", to_retire, "spring"))
    rows.append(stop("retire", "retirement", "retirement", "spring"))

    fields = [
        "slot_id", "region", "branch", "seq", "type", "season",
        "draw_pool", "stop_event", "gate", "notes",
    ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    lines = [",".join(fields)]
    for r in rows:
        lines.append(",".join(str(r[f]) for f in fields))
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")

    path_branches = {
        "youth", "college", "career_track",
        "spine_to_marriage", "open_lone", "spine_to_house1", "spine_to_brawn",
        "open_brawn", "spine_to_child1", "open_scholar", "spine_to_house2",
        "spine_to_child2", "spine_to_house3", "spine_to_social", "open_social",
        "spine_to_child3", "spine_to_midlife", "spine_to_house4", "spine_to_retire",
    }
    fork_names = (
        "college", "career_track", "open_lone", "open_brawn",
        "open_scholar", "open_social",
    )
    path = [r for r in rows if r["branch"] in path_branches or r["type"] in ("stop", "fork")]
    fork_walked = sum(1 for r in path if r["branch"] in fork_names)
    spine_walked = sum(
        1 for r in path
        if r["type"] not in ("stop", "fork") and r["branch"] not in fork_names
    )
    paydays = sum(1 for r in path if r["type"] == "payday")
    actions = sum(1 for r in path if r["type"] == "action")
    print(f"wrote {len(rows)} slots to {OUT}")
    print(f"open-path squares {len(path)}")
    print(f"  spine tiles {spine_walked}  fork tiles {fork_walked}  "
          f"stops {sum(1 for r in path if r['type'] in ('stop','fork'))}")
    print(f"  actions {actions}  paydays {paydays}  "
          f"fork share {fork_walked / (spine_walked + fork_walked):.0%}")


if __name__ == "__main__":
    main()
