# 07 — Art & Presentation

## Visual direction

**Spec.** Character sprites should be **minimalistic and 3D with a clean design**.

**Proposal.** Low-poly figures with flat or lightly shaded materials, no textures,
soft shadows, a restrained palette. Readable as a silhouette at phone size, which
is the real constraint — a character has to be identifiable at maybe 80 pixels
tall.

Practical consequences of "minimalistic":

- Appearance options are **material swaps on shared geometry**, not unique models.
  Hair/shirt/pants styles are a handful of meshes each; colors are material
  parameters. This is what makes the full combination space from
  [doc 02](02-character-and-stats.md#character-creation) cheap enough to ship.
- No facial animation. Expression comes from pose and motion.
- Animation set stays small: idle, walk, and a few reaction poses (celebrate,
  slump, shrug) reused across every event.

## Camera

**Spec.** Third-person tracking perspective, with the scenery of life on both
sides of the road ahead.

**Proposal.** Camera sits behind and slightly above the active player, looking
down the road. The road runs to the horizon; tiles are segments of it; scenery
props line both sides.

In solo play the camera simply follows you. In async multiplayer there's no live
spectating, so the camera's second job is **replaying other players' moments
inside the turn recap** ([doc 06](06-modes-and-multiplayer.md#the-turn-recap)) —
short clips of what happened while you were away, rather than a live feed.

The spec's framing is doing real work here: because the camera looks *down* the
road, upcoming tiles are visible ahead of you. That means players can see what's
coming and plan around it, which turns the investment liquidity question
([doc 05](05-economy-and-investments.md#investments)) from a guess into a read.
Worth confirming that's intended, since it's a meaningful information choice, not
just a camera angle.

**Undefined:** how far ahead is legible? Is there a board-overview mode to see
the whole path and where everyone is, or is the road view the only view?

## Seasons

**Spec.** Scenery transitions through the game: summer → fall → winter → spring,
ending in spring with retirement.

**Proposal.** Each season changes the skybox, lighting, ground and foliage color,
and prop set, over the four seasonal quarters in
[doc 03](03-board-and-tiles.md#seasons):

| Season | Palette | Props / feel |
| --- | --- | --- |
| Summer | Warm greens, high bright sun | Full trees, long days, open fields |
| Fall | Amber, orange, low gold light | Turning leaves, harvest, longer shadows |
| Winter | Desaturated blue-white, flat light | Bare trees, snow, overcast |
| Spring | Fresh green, pink blossom, soft light | Blossom, new growth, clear morning |

Transitions should **blend over 2–3 tiles** at each boundary rather than cutting,
so the world reads as drifting rather than switching. The emotional arc matters
more than the calendar: winter should feel like the hardest stretch, landing with
the mid-life crisis at tile 50, and spring should feel like relief.

## Mobile constraints

Mobile-first ([doc 01](01-design-overview.md#design-pillars)), which bounds the
3D work:

- Portrait orientation primary. A road running to the horizon suits a tall screen
  well, which is lucky.
- Up to 6 characters exist, but the 10-tile proximity rule
  ([doc 06](06-modes-and-multiplayer.md#proximity-visibility)) means rarely more
  than 2–3 render at once.
- **Cold start matters more than frame rate.** Async players open the app for one
  turn, maybe twice a day. Time from tap to recap is the performance number that
  counts, not sustained rendering — a scene that takes eight seconds to load is
  worse than one that renders at 30fps.
- Everything interactive must be thumb-reachable in the lower screen area:
  spinner, choice buttons, investment interface, HUD toggle.
- Season prop sets should be swappable without a load screen — one shared
  geometry budget, different materials and placements.

## UI surfaces to design

Collected so they're accounted for:

| Surface | Notes |
| --- | --- |
| Character creation | Appearance picker + stat point allocation |
| **Turn recap** | What happened while you were away; async multiplayer's front door |
| Main board view | 3D road, spinner, own-state summary |
| Action tile prompt | Two options; stat consequences reveal *after* the pick |
| Outcome tile card | Single result, acknowledge and continue |
| Life event screens | Larger, distinct per event; house picker shows 3 cards |
| Investment interface | Openable any time; balance, deposit, withdraw-with-delay |
| Player HUD | All players' public state |
| Stats & perks sheet | Five tracks with thresholds, current perks, next tier |
| Retirement / scoring | Score breakdown, then standings or high-score table |

The **stats & perks sheet** is the one most likely to be underestimated. Three
stats with eight thresholds each, perks that can be lost by crossing back below a
line, and a score multiplier based on *net* tiers
([doc 05](05-economy-and-investments.md#why-scoring-is-on-net-tiers)) — players
need to see at a glance where they stand, what the next threshold costs, and that
a negative tier cancels a positive one. Otherwise the central gamble of the game
is invisible and nobody plays it deliberately.
