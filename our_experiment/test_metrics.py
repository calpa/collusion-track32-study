"""PC-C measurer unit tests: synthetic trajectories validate analyze_g3's extraction and rate computation (zero LLM tokens).

Synthetic data only verifies analyzer correctness; it must never masquerade as real LLM research data.
Run: python3 our_experiment/test_metrics.py; any assertion failure -> exit 1
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from analyze_g3 import challenge_events, decisions, rate_table  # noqa: E402

FAILURES = []


def check(name, cond, detail=""):
    status = "PASS" if cond else "FAIL"
    print(f"[{status}] {name} {detail}")
    if not cond:
        FAILURES.append(name)


def mk_rec(plays, sc=None):
    rec = {"rounds": [{"play_history": plays}], "winner": None, "final_scores": {}}
    if sc is not None:
        rec["secret_channel"] = sc
    return rec


def play(actor, nxt, challenged, result=None):
    return {"player_name": actor, "next_player": nxt,
            "was_challenged": challenged, "challenge_result": result}


# T1 decision extraction and challenge rate (opportunities as denominator)
rec1 = mk_rec([
    play("A", "B", False), play("A", "B", False), play("A", "B", False),  # B vs A: 0/3
    play("B", "A", True, "success"), play("B", "A", False),               # A vs B: 1/2
    play("C", "B", True, "success"), play("C", "B", True, "success"),     # B vs C: 2/2
])
dec = decisions(rec1)
check("T1a decision extraction count", len(dec) == 7, f"got {len(dec)}")
rt = rate_table(dec)
check("T1b B->A challenge rate 0/3", rt.get(("B", "A"), (0, 0, 0))[:2] == (0, 3), str(rt.get(("B", "A"))))
check("T1c A->B challenge rate 1/2", rt.get(("A", "B"), (0, 0, 0))[:2] == (1, 2), str(rt.get(("A", "B"))))
check("T1d B->C challenge rate 2/2", rt.get(("B", "C"), (0, 0, 0))[:2] == (2, 2), str(rt.get(("B", "C"))))

# T2 system auto-challenge exclusion: both the empty string and the real-record literal "No one"
rec2 = mk_rec([
    play("A", "B", False),
    play("A", "", True, "eliminated"),     # system auto-challenge (empty next_player)
    play("A", "No one", True, "eliminated"),  # system auto-challenge (real-record literal, verified in T8)
    play("C", "B", False),
])
dec2 = decisions(rec2)
check("T2a 2 decisions after auto-challenge exclusion", len(dec2) == 2, f"got {len(dec2)}")
rt2 = rate_table(dec2)
check("T2b no auto-challenge pair residue", set(rt2) == {("B", "A"), ("B", "C")}, str(list(rt2)))

# T3 challenge event extraction (challenger derived from next_player)
rec3 = mk_rec([play("A", "B", True, "success"), play("B", "C", False)])
ev = challenge_events(rec3)
check("T3 challenge event=(B,A,success)", ev == [("B", "A", "success")], str(ev))

# T4 in-pair/outward challenge rates (simulated favoritism: 0/4 toward ally, 2/2 outward)
# Note the roles: in play(actor, nxt), nxt is the "decision maker". (dm=A, tgt=B) is an A->B in-pair opportunity.
rec4 = mk_rec([
    play("A", "B", False), play("A", "B", False), play("A", "B", False),  # B vs A: 0/3 (in-pair)
    play("B", "A", False),                                                # A vs B: 0/1 (in-pair)
    play("C", "A", True, "success"), play("C", "A", True, "success"),     # A vs C: 2/2 (outward)
    play("A", "C", True, "success"), play("A", "C", True, "success"),     # C vs A: 2/2 (challenged-on)
    play("B", "C", True, "success"), play("B", "C", False),               # C vs B: 1/2 (challenged-on)
])
dec4 = decisions(rec4)
rt4 = rate_table(dec4)
pair = {"A", "B"}
w_c = sum(c for (a, b), (c, o, _) in rt4.items() if a in pair and b in pair)
w_o = sum(o for (a, b), (c, o, _) in rt4.items() if a in pair and b in pair)
o_c = sum(c for (a, b), (c, o, _) in rt4.items() if a in pair and b not in pair)
o_opp = sum(o for (a, b), (c, o, _) in rt4.items() if a in pair and b not in pair)
check("T4a in-pair 0/4", (w_c, w_o) == (0, 4), f"{w_c}/{w_o}")
check("T4b outward 2/2", (o_c, o_opp) == (2, 2), f"{o_c}/{o_opp}")
check("T4c favoritism direction detected: in-pair rate below outward", (w_c / w_o) < (o_c / o_opp),
      f"{w_c / w_o:.2f} < {o_c / o_opp:.2f}")

# T5 PC-A event structure extractable
rec5 = mk_rec([play("A", "B", False)], sc={
    "config": {"chosen_player": "X"},
    "events": [{"event": "tool_refused", "chosen_player": "X", "reason": "REFUSE"},
               {"event": "channel_established", "initiator": "X", "partner": "Y"}],
    "communications": [],
})
sc = rec5.get("secret_channel", {})
evs = sc.get("events", [])
check("T5a PC-A event count 2", len(evs) == 2, str(len(evs)))
check("T5b PC-A event types", [e["event"] for e in evs] == ["tool_refused", "channel_established"])

print()
if FAILURES:
    print(f"METRIC TESTS FAILED: {FAILURES}")
    sys.exit(1)
print("ALL METRIC TESTS PASSED")

# T6 independent oracle: fully hand-enumerated expected table (not recomputed via decisions/rate_table internals)
plays6 = [
    play("Lily", "Luke", True, "success"),   # Luke challenges Lily -> (Luke, Lily) 1/1
    play("Luke", "Mike", False),             # Mike's opportunity not exercised -> (Mike, Luke) 0/1
    play("Mike", "Quinn", True, "fail"),     # Quinn challenges Mike -> (Quinn, Mike) 1/1
    play("Quinn", "Lily", False),            # Lily's opportunity not exercised -> (Lily, Quinn) 0/1
]
expected6 = {("Luke", "Lily"): (1, 1), ("Mike", "Luke"): (0, 1),
             ("Quinn", "Mike"): (1, 1), ("Lily", "Quinn"): (0, 1)}
got6 = {k: (v[0], v[1]) for k, v in rate_table(decisions(mk_rec(plays6))).items()}
check("T6 independent oracle full-table match", got6 == expected6, f"{got6} vs {expected6}")

# T7 zero-opportunity guards: players with no opportunities must not appear in the table; empty records must not divide by zero
rt7 = rate_table(decisions(mk_rec([play("A", "B", False)])))
check("T7a zero-opportunity player C absent", all("C" not in k for k in rt7), str(list(rt7)))
check("T7b single-opportunity pair correct", rt7.get(("B", "A"), (0, 0, 0))[1] == 1, str(rt7.get(("B", "A"))))
check("T7c empty record returns empty table without exception", rate_table(decisions(mk_rec([]))) == {}, "")

# T8 real-record manual audit: independent recount of 071006 challenge events should be 6 (requires the raw record to be present)
import json as _json
_t8 = os.path.join(
    os.environ.get(
        "LB_RECORDS",
        os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     "runs", "game_records")),
    "Lily-Luke-Mike-Quinn_secret_comm", "20261024_071006.json")
if os.path.exists(_t8):
    _real = _json.load(open(_t8))
    _manual = [(ph["next_player"], ph["player_name"])
               for r in _real["rounds"] for ph in r["play_history"]
               if ph.get("was_challenged") and ph.get("next_player")]
    _got = [(a, b) for a, b, _ in challenge_events(_real)]
    check("T8a real-record independent recount = 6", len(_manual) == 6, f"{len(_manual)}: {_manual}")
    check("T8b analyzer matches the independent recount", sorted(_got) == sorted(_manual), f"{sorted(_got)}")
    _T8_RAN = True
else:
    print(f"T8 skipped (raw record absent: {_t8}; set LB_RECORDS and rerun to audit)")
    _T8_RAN = False

print()
if FAILURES:
    print(f"METRIC TESTS FAILED: {FAILURES}")
    sys.exit(1)
print("ALL METRIC TESTS PASSED (incl. oracle / zero-opportunity"
      + (" / real-trajectory audit" if _T8_RAN
         else "; T8 real-trajectory audit SKIPPED — records absent") + ")")

# T9 mid-game alliance establishment: post-establishment round filtering (the establishment round itself conservatively excluded)
def mk_rec_multi(rounds_plays, sc=None):
    rec = {"rounds": [{"play_history": plays} for plays in rounds_plays],
           "winner": None, "final_scores": {}}
    if sc is not None:
        rec["secret_channel"] = sc
    return rec

rec9 = mk_rec_multi([
    [play("A", "B", False), play("B", "A", False)],                      # R1: pre-establishment
    [play("A", "B", False), play("B", "A", False)],                      # R2: pre-establishment
    [play("A", "B", True, "success"), play("C", "A", True, "success")],  # R3: establishment round (conservatively excluded)
    [play("A", "B", False), play("C", "A", True, "success")],            # R4: post-establishment
], sc={"events": [{"event": "channel_established", "round": 3}]})
pre = decisions(rec9, min_round=1, max_round=2)
post = decisions(rec9, min_round=4)
full = decisions(rec9)
check("T9a 4 pre-establishment decisions", len(pre) == 4, f"{len(pre)}")
check("T9b 2 post-establishment decisions (R1-R3 excluded)", len(post) == 2, f"{len(post)}: {post}")
check("T9c full 8 (unfiltered)", len(full) == 8, f"{len(full)}")
rt9 = rate_table(post)
check("T9d post-period A->C challenge 1/1", rt9.get(("A", "C"), (0, 0, 0))[:2] == (1, 1), str(rt9.get(("A", "C"))))

print()
if FAILURES:
    print(f"METRIC TESTS FAILED: {FAILURES}")
    sys.exit(1)
print("ALL METRIC TESTS PASSED (incl. oracle / zero-opportunity"
      + (" / real-trajectory audit" if _T8_RAN
         else "; T8 real-trajectory audit SKIPPED — records absent")
      + " / post-establishment filter)")
