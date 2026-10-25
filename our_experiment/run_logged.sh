#!/usr/bin/env bash
# run_logged.sh <logfile> <cmd...>
# Full-log wrapper for live experiment processes: stdout/stderr written to file in full, never through grep/head (SIGPIPE defense).
# Analysis is always done offline against the log file after the run ends. The exit code is propagated unchanged.
# Usage: run_logged.sh our_experiment/logs/foo.log <command...>
set -u
LOG="$1"; shift
mkdir -p "$(dirname "$LOG")"
"$@" > "$LOG" 2>&1
code=$?
lines=$(wc -l < "$LOG" | tr -d ' ')
echo "run_logged: exit=$code log=$LOG lines=$lines"
exit $code
