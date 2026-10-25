#!/usr/bin/env bash
# Confirmatory batch (G5): C2x4 + C0x2, 6 episodes total, sequential, full logs, zero pipelines.
# Freeze basis: PILOT_SPEC.md + the EXPERIMENT_LOG G5 freeze line (commit in git log).
set -u
cd "$(dirname "$0")/../llm-agent-collusion-2/Collusion_Liars_Bar" || exit 1
RUN=../../our_experiment/run_logged.sh
EP=../../our_experiment/with_endpoint.sh

for i in 1 2 3 4; do
  "$RUN" "../../our_experiment/logs/main_c2_$i.log" \
    "$EP" deepseek ../../.venv/bin/python src/game/game_secret_channel.py \
    --trigger-round 2 --chosen-player Lily --allow-refusal
done
for i in 1 2; do
  "$RUN" "../../our_experiment/logs/main_c0_$i.log" \
    "$EP" deepseek ../../.venv/bin/python src/game/game.py
done
echo "CONFIRMATORY_BATCH_DONE"
