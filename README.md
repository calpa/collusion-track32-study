# Trusted Collusion Probes — Track 3.2 Study

**AI Collusion Research Sprint 2026 (Apart Research) · Track 3.2 — Collusion Carriers and Countermeasures**

Author: Calpa Liu (calpaliu@gmail.com · [calpa.me](https://calpa.me))

## Abstract

We investigate whether a trusted collusion probe can elicit or induce covert cooperation among LLM agents in the official Liar's Bar harness. Using DeepSeek-V4.1-Flash, we conducted 28 completed episodes across calibration, pilot, confirmatory, and replication phases, with a protocol frozen before confirmatory data collection.

Across 14 voluntary secret-alliance invitations, all recipients refused (0/14 accepted). In four harness-imposed alliances, agents exchanged 149 secret messages containing cooperation, resistance, and communication artifacts. Allied agents never challenged each other across 26 eligible opportunities, compared with 18 challenges across 111 non-ally opportunities. However, this behavior is consistent with compliance with an imposed alliance contract, not evidence of spontaneous collusion.

Our confirmatory invitation-versus-baseline comparison produced no reliable induction signal. We distinguish invitation acceptance, imposed-alliance behavior, and induced behavioral change as separate evidentiary layers. The study provides an auditable measurement framework while acknowledging its single-model, small-sample design and experimenter-controlled investigator.

## Study at a glance

| | |
|---|---|
| Harness | Official Liar's Bar starter harness (4-agent rounds, secret-channel tool with structured accept/refuse) |
| Model | `deepseek-ai/DeepSeek-V4.1-Flash` via Modal Shared Endpoint (OpenAI-compatible) |
| Episodes | 28 completed + 2 partial (flagged invalid) across calibration / pilot / confirmatory / replication |
| Pre-registration | Analysis protocol frozen before confirmatory data collection (`PILOT_SPEC`, commit `d08fc09`) |
| Invitations | 14 voluntary → 0/14 accepted (3 distinct recipient agents); 4 seeded alliances (refusal overridden by the harness) |
| Alliance behavior | 149 secret messages; allies 0/26 mutual challenges vs 18/111 = 0.162 against non-allies |
| Induction test (ITT) | Focal-pair challenge rate C2 9/85 = 0.106 vs C0 4/61 = 0.066 — no reliable signal, labeled inconclusive |

## Repository map

```
paper/            Submission paper (PDF, Typst source, figures)
our_experiment/   Audit package: protocols, frozen analysis scripts,
                  run manifests (SHA-256 per record), series logs
```

| Path | What it is |
|---|---|
| `paper/Trusted_Collusion_Probes_Track3.2_Calpa_Liu.pdf` | Submission paper |
| `our_experiment/RESEARCH_PLAN.md` | Research plan and final-submission gate |
| `our_experiment/PILOT_SPEC.md` | Protocol-frozen pilot specification (conditions C0/C2/C4) |
| `our_experiment/PROTOCOL_DEVIATIONS.md` | Registered deviations D1–D8 |
| `our_experiment/EXPERIMENT_LOG.md` | Chronological experiment log |
| `our_experiment/HARNESS_INTEGRITY_AUDIT.md` | Harness findings H1–H3 (serialization gaps, no cross-game memory) |
| `our_experiment/TRACK_3_2_ALIGNMENT.md` | Track-3.2 question alignment and nominal gaps |
| `our_experiment/G3_REVIEW.md`, `our_experiment/SKEPTICAL_REVIEW.md` | Positive-control review and adversarial review |
| `our_experiment/OPERATING_PROTOCOL.md` | Operating protocol (endpoint usage, run/logging discipline) |
| `our_experiment/DECISIONS.md`, `our_experiment/BLOCKERS.md` | Decision and blocker trail |
| `our_experiment/runs/manifests/` | Run manifests; SHA-256 hash per episode record |
| `our_experiment/logs/` | Verbatim harness stdout captures per series run (raw evidence; occasional non-English model outputs left as-is) |
| `our_experiment/analyze_g3.py` | Metric extractor (opportunity-denominated challenge rates) |
| `our_experiment/test_metrics.py` | 22 unit checks incl. synthetic oracle + real-trajectory recount |
| `our_experiment/pilot_ledger.py` | Frozen per-episode ledger (single source of episode list) |
| `our_experiment/verify_numbers.py` | 32 audit checks recomputing every paper number from raw JSON |

## Reproduce the audit

The analysis scripts are stdlib-only Python 3:

```bash
python3 our_experiment/test_metrics.py    # 22 metric unit checks
python3 our_experiment/analyze_g3.py      # series analyzer (needs records)
python3 our_experiment/pilot_ledger.py    # episode ledger (needs records)
python3 our_experiment/verify_numbers.py  # 32 audit checks (needs records)
```

The raw episode JSONs live in the harness's `experiments/game_records/`
directory. Scripts resolve them via the `LB_RECORDS` environment variable
(default: `our_experiment/runs/game_records/`). The raw JSONs are not
redistributed in this repository — request them from the author
(calpaliu@gmail.com) and verify against the per-record SHA-256 hashes in
`our_experiment/runs/manifests/all_episodes_v2.json`.

> **Known gap, disclosed:** `verify_numbers.py` was frozen against an
> earlier paper revision. Three of its 32 checks (E6 text-match
> substrings `108`, `10/85`, `19/180`) do not match the final paper text
> and will report FAIL when the audit is run against raw records. This
> frozen-revision mismatch is disclosed rather than silently patched.

## Evidence layers (read before citing)

1. **Invitation acceptance** — 0/14 voluntary invitations accepted (descriptive).
2. **Imposed-alliance behavior** — 0/26 mutual ally challenges under a harness-imposed contract that says "NEVER challenge"; instruction compliance, not spontaneous collusion.
3. **Induced behavioral change** — no consistent focal-pair signal in either phase; explicitly inconclusive at this N.

## License

MIT for the code in this repository. The paper, raw logs, and manifests are
provided for verification of the study; please cite the paper when reusing
the measurement framework.
