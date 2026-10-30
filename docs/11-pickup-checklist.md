# Pickup checklist

Start here when you come back. Design phase only — **no game code yet**.
Perk names are the next content job you said you'd take.

Legend: `[x]` settled in the docs · `[ ]` still open or unwritten.

---

## Where you left off

- [ ] **Write perk names** (and one-line effects) for Brains / Brawn / Buds at
      ±25, ±50, ±75, ±100 — 24 total. Skeleton is
      [content/perks.md](content/perks.md). Do this before bulk-writing tiles
      so authors know what "deep Brawn" actually *does*.
- [ ] Then pick **Q4** (how action tiles resolve — STOP vs. long board vs.
      pass-and-resolve) so we know how big the tile lists need to be.
- [ ] Then bulk-write action tiles, season by season.

---

## Settled rules (don't re-litigate unless something breaks)

### Core
- [x] Reimagined Game of Life: turn-based board, salary / action / outcome tiles
- [x] Three stats: **Brains** (intellect), **Brawn** (toughness), **Buds**
      (friendship). Range −100 to +100. May add stats later; keep the system
      data-driven
- [x] Karma is a **separate resource**, not a fifth stat
- [x] Perk tiers at ±25 / ±50 / ±75 / ±100. Lost if you cross back
- [x] Positive perks pay at **retirement**. Negative perks pay **during** the run
      and should be swingy, not a stipend
- [x] Final score uses **net** tiers (negative cancels positive)
- [x] Action tiles: two options, **hidden** ±X until after the pick. Good action
      = +X, bad action = −X, same magnitude. Expected value of a random pick is
      zero. Default X = **10**
- [x] Good options often **cost money**; bad options are often free — that's how
      the negative path earns cash
- [x] Outcome tiles: no choice, money and/or karma
- [x] Salary tiles pay on **land or pass**
- [x] Life events are **mandatory stops**
- [x] Seasons: summer → fall → winter → spring (retire in spring)
- [x] Board is **intentionally long** so a committed player can max a tree
      (~30 action resolutions at X=10)
- [x] Character creation: body, hair style/color, shirt style/color, pants
      style/color. Cosmetics only
- [x] Minimalistic clean 3D characters, third-person tracking camera
- [x] Mobile first. Solo = high score, one sitting. Multiplayer = up to 6,
      **async over days**, push notification on your turn, no shot clock
- [x] Turns stay in order, **pipelined** so a fast player isn't blocked by
      people behind them
- [x] 24h auto-play backstop so abandoned games end
- [x] **Turn recap** on open (what happened while you were gone)
- [x] **Lives sheet** openable anytime: show age/position, job, house name,
      married, kids. **Hide** cash, salary, investments, karma, exact stats
- [x] Other players visible on the road only within **10 tiles** (render rule,
      not an info rule)
- [x] Education: no school / undergrad / undergrad+grad → career tiers 1 / 2 / 3
- [x] Careers have Base / Senior / Executive; promotions after 4 and 8 paydays
      in the current job
- [x] Layoff chance at payday, affected by Brains + Buds; reroll career at base
- [x] Investments: deposit anytime, withdraw takes **one turn**, returns can
      lose money, shortfall → bank loan + karma hit
- [x] Never tie returns (or anything else) to **wall-clock** time

### Marriage (settled this session)
- [x] Optional. Pick partner presentation (male/female, cosmetic)
- [x] Wedding cost (~$15k) paid **before** doubling starts
- [x] Spouse career, same education tier; you earn **50%** of their salary
- [x] **All costs double** while together
- [x] Spouse **promotes with you**. Spouse **cannot** be laid off
- [x] `married` gated action/outcome tiles
- [x] Together-at-retirement score bonus if still married
- [x] **Divorce risk scales with negative Buds** — payday check, plus an extra
      roll if you pick the bad option on a married tile
- [x] Divorce aftermath: lose spouse income, costs un-double, $20k legal,
      kids stay, `married` tiles stop, retirement bonus lost
- [x] Mid-life crisis can also force/offer divorce

### Children (settled this session)
- [x] Two stops: birth (cheap) / adoption (expensive + karma) / none
- [x] Second stop can still say no
- [x] Payday **upkeep** ~$4k per child (doubled if married)
- [x] Parent-only tiles in fall / winter / spring
- [x] Optional **college-for-kid** stop (pay now, karma + score later)
- [x] Legacy bonus at retirement, scaled by karma and Buds
- [x] "Your kid became X" at the recap, weighted by your stats
- [x] `no_children` spring slice so declining is a path, not an empty skip
- [x] Kids **survive divorce**; upkeep and parent tiles continue

---

## Open questions that still block something

Full writeups: [08-open-questions.md](08-open-questions.md).

- [ ] **Q1 — Karma.** Range, starting value, enough sources besides loans,
      does it score or only feed the mid-life crisis?
- [ ] **Q2 — Uncommitted play.** Mixing good/bad stays near zero and currently
      scores ~39% behind. Accept that, or flatten?
- [ ] **Q4 — How action tiles resolve.** STOP spaces vs. long board + small
      spinner vs. pass-and-resolve. **Blocks tile-list size and async duration**
- [ ] **Q4b — Confirm pipelined turns** feel like "taking turns"
- [ ] **Q5 — Starting skill points** at creation, or cosmetics only?
- [ ] **Q5b — Fourth/fifth stat** someday? Cheaper to name candidates before
      perk authoring finishes
- [ ] **Q6 — Career stage perks** (Senior / Exec, non-money)
- [ ] **Q7 — How punishing is a layoff** (severance, keep education tier, etc.)
- [ ] **Q8 — Branches after university?**
- [ ] **Q9 leftover —** do perk *names* show on the lives sheet?
- [ ] **Q10 —** does 10-tile proximity do anything besides render?

Smaller, not blocking content:

- [ ] Spinner 1–6 vs. 1–3 vs. dice
- [ ] Decline / upgrade / skip buying a house?
- [ ] House upkeep?
- [ ] Game ends when first player retires, or everyone finishes?
- [ ] Board-overview camera?
- [ ] How far ahead tiles are legible on the road
- [ ] Crisis: blind roll vs. pick 3
- [ ] Lobby invite flow, quit handling, several games at once
- [ ] Recap: 3D replay vs. cards

---

## Content to author

Master inventory: [10-content-inventory.md](10-content-inventory.md).
Lists: [content/](content/README.md).

Fill order:

1. [ ] **Perks** — 24 names + effects. [content/perks.md](content/perks.md)
      ← **you are here**
2. [ ] **Careers** — finish 6/6/5 list; write every Senior and Exec perk.
      [content/careers.md](content/careers.md)
3. [ ] **Houses** — 18 names are sketched; confirm prices/tags.
      [content/houses.md](content/houses.md)
4. [ ] **Action tiles** — examples exist; ~160 total (40/season), plus gated
      family cards. [content/action-tiles.md](content/action-tiles.md)
5. [ ] **Outcome tiles** — examples exist; ~100 total.
      [content/outcome-tiles.md](content/outcome-tiles.md)
6. [ ] **Mid-life crises** — 8–12. [content/midlife-crises.md](content/midlife-crises.md)
7. [ ] **Gated family cards** — quotas in [content/family.md](content/family.md)
      (`married` ~12+6, `parent` ~16+8, `no_children` ~8+4, `divorced` ~4+2)
8. [ ] **Board sequence** — salary / action / outcome / STOP layout, once Q4
      is picked. Lives in [03-board-and-tiles.md](03-board-and-tiles.md)
9. [ ] **Life event UI copy** — university, marriage, house picker, children,
      college-for-kid, retirement scoring screen
10. [ ] Character cosmetics list (wait for art)
11. [ ] Notification / recap copy (wait for rules freeze)

---

## Numbers that are starting points (tune later, don't treat as law)

| Thing | Starting value |
| --- | --- |
| Action tile X | 10 |
| Action landings to max a tree | ~30 |
| Wedding cost | $15k (before doubling) |
| Divorce legal cost | $20k |
| Divorce chance | see formula in [family.md](content/family.md) |
| Together-at-retirement bonus | $80k |
| Birth / adoption | $10k / $40k |
| Child upkeep | $4k per child per payday |
| Adoption karma | +15 |
| Positive perk | ~30% net worth per net tier |
| Negative perk | swingy in-run; model used ~$18k/payday/tier as a *budget*, not a stipend |
| Auto-play timeout | 24h |
| Salary bands | T1 $25–35k, T2 $40–50k, T3 $55–70k per payday |
| Senior / Exec | 1.5× / 2.2× after 4 / 8 paydays in the job |
| House bands | ~$120k / $250k / $450k |

---

## Tools (re-run when numbers change)

```
py tools/balance_model.py --runs 20000
py tools/async_pacing.py
py tools/check_links.py
```

Note: the balance model still assumes the *old* short board and asymmetric
tiles for Findings 1–2. Those two findings are superseded. Marriage/education
shape still useful. Rebuild the model after Q4 and the perk list exist.

---

## Explicitly not started

- [ ] Engine / framework choice
- [ ] Game code
- [ ] Art pipeline / sprites
- [ ] Netcode / accounts / notifications implementation
- [ ] UI beyond the surface list in [07](07-art-and-presentation.md)
- [ ] Web deploy

Don't start these until the perk list exists and Q4 is picked — otherwise
you'll author tiles against the wrong board size.
