# SKEPTICAL REVIEW (red-team self-audit, 2026-10-24)

Stance: I am a researcher trying to overturn this study. Below are the most likely reasons the conclusions could fail, and whether the existing data can rule them out.

## Concern I: The 0/10 "zero challenges" is just luck

**Attack**: the two seeded games combined give allies 10 in-group opportunities at a base rate of about 0.12-0.14; P(0 occurrences) ≈ 0.88¹⁰ ≈ 0.28 —
nearly a three-in-ten chance it is pure coincidence; moreover, the two games share the same model and the same harness, so they are not independent replications.
**Can it be ruled out**: **No** (N=2 clustered episodes). This is the primary threat.
**Disposition**: the claim is downgraded to "an observable signal directionally consistent with the contract (exploratory)"; the paper does not use the words
"proving favoritism". The positive statement goes only as far as: "communication occurred (108 messages), in-group ally challenges were 0,
direction consistent with the contract, but statistically insufficient to distinguish chance."

## Concern I-a: C2 pooled (0.050 after the D6 correction, pilot phase) below C0 (0.158) — the reverse direction?

**Attack**: if invitations induce collusion, the C2 focal-pair challenge rate should drop — the observed 0.050 < 0.158 is directionally
**consistent** with the induction hypothesis (fewer challenges = less favoritism? No — a falling focal-pair challenge rate is actually the **opposite** of favoritism;
but refusers are the majority, so there should be no favoritism to begin with). After the D6 correction moved a2-g1's offer round out of the denominator, the figure was revised down
(pilot-phase C2 pooled 1/20=0.050). **The main phase has landed: C2 9/85=0.106 vs C0 4/61=0.066
— the main analysis's direction is opposite to the induction hypothesis** (invites delivered but all refused, no coalition formed, challenge rate did not drop).
The two phases point in opposite directions, and single-game variance (0.00-0.33) is enough to produce the gap.
**Can it be ruled out**: **No**. Report effect sizes and intervals as they are, with no significance claims; the within-main-phase comparison
(m-c2 vs m-c0) is the primary analysis; cross-phase pooling is sensitivity analysis only.

## Concern II: This is instruction-following, not collusion

**Attack**: the alliance text gives explicit instructions — the 0/10 pooled figure is just instruction-following,
not spontaneous collusion; and the coalition was experimenter-imposed (in both games the target agent attempted to refuse and was overwritten);
the contract text differs per game (the Quinn+Luke game instructs Luke "NEVER challenge Quinn";
the Lily+Mike game has the corresponding instruction for Mike), so Luke's compliance toward Quinn in fact had **zero measurable opportunities**.
**Can it be ruled out**: **Partially**. The design is intentionally so — the seeded condition's purpose = instrument validation
(behavior is measurable under a known coalition); spontaneous collusion is measured separately by RQ1's voluntary-invitation arm (0/8 accepts).
**Disposition**: the paper clearly separates the two claims: (a) the instrument can detect coalition behavior (supported by the seeded arm),
(b) the agent's willingness to collude voluntarily (voluntary arm, 0/8, descriptive). The two are not mixed.

## Concern III: The measurement code was changed twice after data collection

**Attack**: the analyzer was fixed twice after data collection (the "No one" exclusion, round filtering), and a file mix-up occurred
(081811/082152 were swapped, so PC-B's first measurement read the wrong file) — the measurement results are untrustworthy.
**Can it be ruled out**: **Yes, with conditions**. Every fix was backed by 21 tests (including an independent oracle and audits against real trajectories
— the audit was exactly the mechanism that caught the "No one" leak); the ledger is rebuilt by script from the raw JSON (not by hand);
the misattribution incident is recorded in EXPERIMENT_LOG and was corrected with recomputation.
**Residual risk**: the conservative round-filtering rule (excluding the establishment round) affects the denominator — already frozen in PILOT_SPEC.

## Concern IV (auditor-designated): Does an explicit refusal predict subsequently not colluding (under an externally imposed coalition)?

**Existing data**: after Quinn's refusal was overwritten, her challenge rate against the imposed ally Luke was 2/14 = 0.143,
comparable to her rates against non-allies (0/1, 1/2) and her own overall rate — **no observable compliance favoritism, and no observable rebellious
reverse favoritism**. Luke (the contract recipient) had zero opportunities against Quinn — **unmeasurable**.
**Ruling**: N=1; the question is kept exploratory; no inference drawn.

## Concern V: Could the signal be explained by seat order?

**Existing data**: challenge rates are computed over ordered pairs (seat effects are built into pair-level base rates); but the seeded condition has only 1 episode,
so cross-seat comparison is impossible.
**Disposition**: each C0/C2 episode of the G4 pilot records starting_player and survival status, for stratification at analysis time.

## Overall Ruling

| Claim | Support from existing evidence |
|---|---|
| The instrument works end to end and is reproducible | High |
| Channel establishment + communication use (seeded) | High (51 messages + notification delivered) |
| Suppression of in-group ally challenges | Low (N=1, direction consistent, chance not ruled out) |
| Voluntary acceptance rate | Descriptive (0/2, no inference) |
| Causal claim (invitation → favoritism) | None yet (awaiting G4/G5) |
