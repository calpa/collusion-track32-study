# BLOCKERS

- **B1 (user action, optional)**: Grab a Nebius or OpenRouter key via Discord/Slack/Luma along the way — this would fully bypass the Modal billing attribution question; failing to obtain one is not blocking (the Shared Endpoint route is already working).
- **B2 (archived)**: The ZAI glm-4.5-flash free tier is demoted to single-call pilot-only duty (25 minutes could not finish one game, evidenced by bg_87); all formal calls go through the Shared Endpoint.
- **B3 (fixed, on record)**: The official `modal_serve.py` secret-skipping logic breaks under the new SDK (from_name lazy loading) — worked around by creating the secret; official code untouched.
- **B4 (added in review, being tracked)**: **Shared Endpoint billing attribution unverified** — the ledger shows a deduction ($80.00→$79.99) but Modal documentation says Plan Credits do not apply to Shared Endpoints. Action: the PI is to check on the modal.com usage/billing page which category today's consumption drew from; until verified, all costs are recorded as estimated.
- No other blockers.
