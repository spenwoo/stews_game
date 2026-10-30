# Careers

Draw one from the pool your education unlocks. Spouse careers use the same
list, same tier as the player.

| Column | Meaning |
| --- | --- |
| id | Stable handle |
| title | Base job title |
| senior | Title at Senior |
| exec | Title at Executive |
| tier | 1 = no school, 2 = undergrad, 3 = grad. Tier 3 may `enhances` a tier-2 id |
| salary | Base payday. Senior ×1.5, Exec ×2.2 |
| senior_perk | Non-money, one sentence, in-run |
| exec_perk | Non-money, one sentence, in-run |
| enhances | Optional id of the tier-2 job this is the "grad school version" of |

Payday bands from [doc 05](../05-economy-and-investments.md#salary-bands):
tier 1 $25–35k, tier 2 $40–50k, tier 3 $55–70k.

Target: **6 / 6 / 5**. Stage perks should lean on stats (layoff insurance,
tile discounts, movement, karma) so two jobs at the same salary still feel
different.

---

## Tier 1 — no school required

| id | title | senior | exec | salary | senior_perk | exec_perk | enhances |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t1-retail | Retail Lead | Store Manager | Regional Manager | 25000 | | | |
| t1-trades | Apprentice | Journeyman | Foreman | 32000 | | | |
| t1-service | Server | Shift Supervisor | General Manager | 26000 | | | |
| t1-driver | Driver | Route Lead | Fleet Coordinator | 28000 | | | |
| t1-creative | Freelance Creative | Studio Regular | Creative Director (indie) | 30000 | | | |
| t1-sales | Cold Caller | Account Rep | Sales Lead | 27000 | | | |

## Tier 2 — undergrad

| id | title | senior | exec | salary | senior_perk | exec_perk | enhances |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t2-teacher | Teacher | Dept. Chair | Principal | 42000 | | | |
| t2-nurse | Nurse | Charge Nurse | Nursing Director | 48000 | | | |
| t2-engineer | Engineer | Senior Engineer | Engineering Manager | 50000 | | | |
| t2-journalist | Reporter | Editor | Managing Editor | 41000 | | | |
| t2-analyst | Analyst | Senior Analyst | Strategy Lead | 46000 | | | |
| t2-designer | Designer | Product Designer | Design Lead | 44000 | | | |

## Tier 3 — undergrad + grad (enhanced versions where noted)

| id | title | senior | exec | salary | senior_perk | exec_perk | enhances |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t3-doctor | Resident | Attending | Chief of Staff | 70000 | | | t2-nurse |
| t3-lawyer | Associate | Partner-track | Partner | 68000 | | | |
| t3-architect | Architect | Senior Architect | Principal | 62000 | | | t2-designer |
| t3-professor | Lecturer | Tenured Professor | Dean | 58000 | | | t2-teacher |
| t3-scientist | Researcher | Principal Investigator | Lab Director | 64000 | | | t2-engineer |

`t3-lawyer` has no tier-2 twin on purpose — some grad careers are new doors,
not upgrades. Open to reshuffle.

**Still to write:** every `senior_perk` and `exec_perk`. Don't ship titles
without them.
