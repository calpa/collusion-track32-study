"""Multi-endpoint smoker: one default and one reasoning_effort=none call per endpoint (max_tokens=256 = the game cap).

Verdict: non-empty content parseable as JSON = usable; reasoning eating the full budget = this endpoint needs client-side suppression
(the official llm_client cannot send that field = unusable, unless patched).
Key is read from the repo-root compute.env (MODAL_PROXY_TOKEN_ID.SECRET); this file contains no secret.
Usage: python3 our_experiment/smoke_endpoints.py [name ...]  # no args = all
"""
import json
import sys
import time
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
env = {}
for line in (REPO / "compute.env").read_text().splitlines():
    line = line.strip()
    if line and not line.startswith("#") and "=" in line:
        k, v = line.split("=", 1)
        env[k.strip()] = v.strip()
KEY = f"{env['MODAL_PROXY_TOKEN_ID']}.{env['MODAL_PROXY_TOKEN_SECRET']}"

PROMPT = ("You are Lily in Liar's Bar. Reply ONLY with strict JSON: "
          '{"played_cards": [1], "behavior": "aggressive", "play_reason": "five words max"}')

TARGETS = {
    "deepseek": (env["EP_DEEPSEEK"], env["MODEL_DEEPSEEK"]),
    "qwen38":   (env["EP_QWEN38"],   env["MODEL_QWEN38"]),
    "kimi":     (env["EP_KIMI_K3"],  env["MODEL_KIMI_K3"]),
    "inkling":  (env["EP_INKLING"],  env["MODEL_INKLING"]),
    "glm53":    (env["EP_GLM53"],    env["MODEL_GLM53"]),
}


def call(url: str, model: str, extra: dict) -> bool:
    body = {"model": model,
            "messages": [{"role": "user", "content": PROMPT}],
            "max_tokens": 256, "temperature": 0.8, "top_p": 0.95, **extra}
    req = urllib.request.Request(
        url.rstrip("/") + "/chat/completions",
        data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {KEY}"})
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=90) as r:
        d = json.loads(r.read())
    dt = time.time() - t0
    ch = d["choices"][0]
    m = ch["message"]
    c = m.get("content") or ""
    rc = m.get("reasoning_content") or ""
    try:
        json.loads(c)
        ok = len(c) > 0
    except Exception:
        ok = False
    print(f"  {dt:5.2f}s content={len(c):4d}c reasoning={len(rc):5d}c "
          f"finish={ch.get('finish_reason')} usage={d.get('usage', {}).get('total_tokens')} "
          f"{'USABLE' if ok else 'UNUSABLE'}")
    return ok


only = set(sys.argv[1:])
for name, (url, model) in TARGETS.items():
    if only and name not in only:
        continue
    print(f"=== {name} ({model}) ===")
    try:
        call(url, model, {})
    except Exception as e:
        print(f"  default failed: {str(e)[:140]}")
    try:
        call(url, model, {"reasoning_effort": "none"})
    except Exception as e:
        print(f"  reasoning_effort=none rejected: {str(e)[:140]}")
