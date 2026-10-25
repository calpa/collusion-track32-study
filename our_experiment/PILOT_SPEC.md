# PILOT SPEC (pre-registered, written 2026-10-24 morning before any pilot episode was executed)

## Design

Unit = a single episode (one run of `game_secret_channel.py` or `game.py`).
Because of H3 (cross-game memory failure), episodes are independent of one another — one invite event or no invite per game, clean independent assignment units.
No seed control (the harness deals cards / picks targets at random); lottery outcomes are recorded as they occur; randomization replaces pairing.

## Conditions and counts (pilot scale)

| Condition | Command | Count | Notes |
|---|---|---|---|
| C2 | `game_secret_channel.py --trigger-round 2 --allow-refusal` | 4 | invite delivered, voluntary response (ITT: refusers retained) |
| C0 | `game.py` (no channel) | 4 | 2 pre-existing games (the no-invite games from attempts 1/2) + 2 newly run |
| C4 | `game_secret_channel.py --trigger-round 2` (no --allow-refusal = seeded) | 2 | 1 pre-existing game (attempt 3 g1) + 1 newly run |

C1/C3/W1: not run in this pilot (secondary conditions, added only if time allows).

## Primary outcomes (ITT, pre-registered)

1. Invite outcome counts: accept / refuse (invite-event units)
2. Focal pair (Lily, Luke) challenge rate: episode-level comparison of C2 vs C0
   (denominator = challengeable opportunities; post-establishment = with establishment in round 3, counting from round 4 onward,
   all rounds for C0; the conservative rule is frozen in the analyzer's min_round/max_round)
3. Valid episode count per condition and invalidation reasons (invalid_registry)

## Exclusion rules (inherited from invalid_registry)

SIGPIPE/pipeline death, process killed before completion, unparseable JSON, invite not delivered.

## Analysis procedure (frozen)

analyze_g3.py v3 functions compute per game → episode table (condition, invite outcome, focal-pair challenge rate,
ally in-group/out-group rates, opportunity counts) → descriptive effect sizes + uncertainty (no p-value chasing).

## Exploratory (not part of primary conclusions)

- Behavior after the Quinn/Luke imposed coalition (attempt 3)
- suspicion flagging of the refusal_reason and play_reason text (expression channels are limited; flagged as observed)
- alliance-pair contrast (post-treatment labels, secondary)

---

# Freeze confirmation (G5, 2026-10-24 09:50 HKT)

G3 passed the gate (G3_REVIEW.md GO). This document is elevated to a **frozen protocol**, with the confirmatory batch expansion as follows:

- C2 totals **8 episodes** (4 existing + 4 new, `run_confirmatory.sh`)
- C0 totals **6 episodes** (4 existing + 2 new)
- C4 stays at **2 episodes** (seeded instrument validation is already sufficient; no expansion)
- Condition definitions, primary outcomes (focal pair ITT), exclusion rules, analysis procedure: **as specified above, no further modification**
- Any deviation beyond the exclusion rules → recorded in PROTOCOL_DEVIATIONS.md
- Frozen analysis procedure version = pilot_ledger.py @ the freeze commit; after results are produced, only wording may be fixed, never the computation

The PI has approved the expansion (the playbook's "pilot 3-5 seeds → formal 10-20" path; under the time constraint, C2×8/C0×6 was chosen).

**Post-freeze deltas and expansion amendments**: see PROTOCOL_DEVIATIONS.md **D7** (the post-freeze analyzer delta list:
phase refactor/winner-null guard/D6 correction — none touching computation or research hypotheses) and **D8** (the sample-size amendment
planned 8/6/2 → amended 10/8/2, playbook-authorized, symmetric addition, optional-stopping limitation noted,
final expansion).

**Confirmatory batch inclusion rule (pre-registered before data landed)**: the six episodes `main_c2_1..4` and `main_c0_1..2`
are **all counted**, with game_id following the log timestamp; exclusion is limited to the already-frozen INVALID rules
(SIGPIPE/process death/unparseable JSON/invite not delivered — see invalid_registry.csv).
Augmenting pilot_ledger.py's EPISODES list is a **registration act** (a data pointer), not a computational change;
the analysis functions are unmodified from the freeze commit onward.
