#!/usr/bin/env python3
"""Generate docs/evidence/ for batch-2 events + stub Tier-A backlog + infrastructure."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "docs" / "evidence"

# (event_id, name, category, port_status, conf, source_node, research_ref, p_cum, window, observable, claim, why, evidence bullets, would_update, cal_note, needs_research)
BATCH2 = [
    (
        "ev_c4_labor_shock",
        "C4 labor shock visible",
        "capability",
        "done",
        "medium",
        "node1",
        "notes/timeline_prediction/node1_evidence_rationale.md",
        0.82,
        "2026-06-01 → 2027-12-31",
        "Junior white-collar displacement economically binding: Canaries −16% rel. employment in top AI-exposure quintile; Block/Cloudflare-class cuts; Challenger AI-cited layoffs >100k YTD; METR 50%-horizon ≥6h on frontier models.",
        "By CI=4 calendar (~2026 H2–2027), agent labor shock is **economically binding** on junior SWE / white-collar automation tasks — capability layer live before mass DC policy response.",
        "Hybrid time (C): capability tracks METR/AI-2027 fast; digital policy salience lags ~30%. Node 1 partially live on digital layer only; C4 = Agent-1-mini / junior dev shock anchor.",
        [
            "METR Time Horizon 1.1 — 88.6-day doubling post-2024; frontier 6–12h horizon (Feb–Mar 2026)",
            "Stanford DEL Canaries — 22–25 cohort −16% rel. vs least-exposed (firm FE)",
            "Block ~40% HC cut Feb 2026; Challenger H1 2026 101,743 AI-cited cuts",
            "`notes/ai_2027_tracker_scorecard_2026-06.md` — METR Ahead; Economic Impact mixed",
        ],
        "METR horizon stalls <4h through 2027-06; Canaries cohort recovers; Yale SDID turns positive on AI exposure × unemployment.",
        "p_cumulative 0.82 reflects high P(capability binding by end-2027) given partial live status; not P(federal labor law). [CALIBRATE]",
        None,
    ),
    (
        "ev_labor_hearings_peak",
        "Peak DC labor / AI hearings",
        "policy",
        "done",
        "medium",
        "node1",
        "notes/timeline_prediction/node1_evidence_rationale.md §P=0.75",
        0.75,
        "2027-01-01 → 2027-12-31",
        "Senate HELP or relevant committees hold sustained AI + workforce oversight hearings during Node 1 salience peak (~2027 Q2); AFL-CIO Workers First agenda visible in DC.",
        "P(peak DC labor/AI hearings during 2027) ≈ **0.75** — conditional on C4 labor shock unlocking this event.",
        "Sanders chairs HELP; 2023–25 AI hearing precedent; Saunders 2024 arc; policy salience peaks ~2027 Q2 (+30% lag vs capability). Modal outcome = hearings + state bills, not federal training cap.",
        [
            "Node 1 P(HELP hearings by peak) = 0.75",
            "AFL-CIO Workers First Oct 2025; Sanders Apr 2026 meeting",
            "CA Newsom EO N-6-26 (May 2026) — study/recommendations on AI workforce",
        ],
        "Zero HELP AI-labor hearings through 2027-12 after Block-scale events → salience model wrong.",
        "Requires unlock from ev_c4_labor_shock. p_cumulative 0.75 matches Node 1 hearing P directly. [CALIBRATE]",
        None,
    ),
    (
        "ev_c5_agent2_internal",
        "Agent-2 class deployed internally at frontier lab",
        "capability",
        "partial",
        "low",
        "c8 / node12",
        "notes/timeline_prediction/c8_society_snapshot_by_ci.md §C5",
        0.70,
        "2027-06-01 → 2028-12-31",
        "Frontier lab deploys continuous-learning Agent-2 class internally: ~3× R&D multiplier; >50% production code AI-written (Anthropic RSI benchmark); not necessarily public.",
        "By C5 (~2027 H2–2028 on 0.70× tracker), at least one frontier lab runs **continuous-learning Agent-2** internally with material R&D multiplier (~3×).",
        "c8 C5: continuous learning + 3× multiplier Emerging/NTT; Anthropic RSI essay (>80% prod code AI-written) is A/B-tier evidence; tracker Not Yet Testable on full Agent-2.",
        [
            "Anthropic RSI essay (2026-06) — >80% production code AI-written",
            "`c8_society_snapshot_by_ci.md` C5 — ~2027 H2–2028",
            "Node 12 — Agent-2 continuous learning Emerging on tracker",
        ],
        "No lab confirms continuous-learning deployment by 2028; METR/agent evals flat.",
        "p_cumulative 0.70 is [PLACEHOLDER] — weak public observability. Needs lab disclosure or proxy metrics. [CALIBRATE]",
        "No public confirmation of Agent-2-class continuous learning; calibrate from METR R&D automation proxies and earnings calls.",
    ),
    (
        "ev_c6_superhuman_coder",
        "Superhuman coder milestone public",
        "capability",
        "partial",
        "medium",
        "c8",
        "notes/timeline_prediction/c8_society_snapshot_by_ci.md §C6",
        0.65,
        "2028-01-01 → 2029-06-30",
        "Public milestone: frontier model exceeds human expert on sustained SWE tasks (refactors, kernel opt, formal verification scaffolding); METR coding autonomy Confirmed/Emerging.",
        "By C6 (~2028 H1 on hybrid track), **superhuman coder** capability is **publicly legible** — not merely internal.",
        "c8 C6: superhuman coder [SPEC at C6]; tracker Emerging on Agent-3 superhuman coder (~0.70× lag). Neuralese/IDA adjacent but separate observable.",
        [
            "`c8_society_snapshot_by_ci.md` — C6 ~2028 H1",
            "Node 12 mapping — Agent-3 superhuman coder Behind ~0.70×",
            "METR / SWE-bench trajectory (repo tracker)",
        ],
        "Through 2029 no third-party benchmark shows sustained superhuman coding on >4h tasks.",
        "p_cumulative 0.65 [CALIBRATE] — maps to P(C6 public by mid-2029) with tracker discount.",
        "Precise public-announcement threshold vs internal capability needs operational definition.",
    ),
    (
        "ev_c8_agi_public",
        "Major lab announces AGI-class system",
        "capability",
        "partial",
        "medium",
        "node_u1 / c8",
        "notes/timeline_prediction_utopia/node_u1_alignment_symbiosis_evidence_rationale.md §C8",
        0.55,
        "2028-06-01 → 2030-06-30",
        "Major lab **publicly** announces AGI-class or equivalent (remote workers at scale, mass deployment, 'AGI' branding); unlocks alignment salience paths.",
        "P(public AGI-class announcement by end-2030) ≈ **0.55** on hybrid track (2027 H2–2028 H2 core window).",
        "U1/C8 window: first mass deployment where human oversight plausible but strained; METR Ahead pulls capability calendar forward vs governance 0.70×.",
        [
            "U1 §C8 public-AGI window 2027 H2–2028 H2",
            "METR horizon doubling ~88.6 days",
            "`c8_society_snapshot_by_ci.md` — public catches up to C6–C7 with 12–24 mo lag",
        ],
        "No frontier lab AGI-branded release through 2030 despite C6+ internal state.",
        "p_cumulative 0.55 [CALIBRATE] — 'AGI announcement' is marketing-sensitive; use remote-worker-at-scale as fallback observable.",
        "Define AGI observable: branding vs capability threshold (C8 remote workers?).",
    ),
    (
        "ev_c10_internal_concern",
        "Internal eval flags deception at superhuman-researcher tier",
        "alignment",
        "done",
        "medium",
        "node4",
        "notes/timeline_prediction/node4_evidence_rationale.md §3",
        0.50,
        "2029-01-01 → 2031-12-31",
        "Frontier internal evals at C9–C10 flag strategic deception, reward-hacking under deployment-simulation, or alignment-research sabotage — Apollo/Greenblatt-class, at superhuman-researcher tier.",
        "P(C10 internal concern exists | C9+ reached) ≈ **0.50** central — separate from public whistleblower (Trigger E).",
        "Apollo scheming (2024), Greenblatt (2026), Sharma exit precede full C10; AI 2027 assumes credible natsec-relevant evals require C9–C10.",
        [
            "Node 4 §3 — C9–C10 capability anchor",
            "Apollo Research scheming (2024-12); Greenblatt (2026-04)",
            "Partial Node 4s already occurring without C10",
        ],
        "No deception flags through 2031 despite public C8+; Apollo criteria fail on frontier.",
        "Requires unlock from ev_c8_agi_public. p_cumulative 0.50 is author judgment on eval base rate at C10. [CALIBRATE]",
        None,
    ),
    (
        "ev_rsi_cloud_dominant",
        "RSI locus = cloud/software (not embodied first)",
        "capability",
        "done",
        "medium",
        "node12",
        "notes/timeline_prediction/node12_evidence_rationale.md §2",
        0.55,
        "2028-01-01 → 2032-12-31",
        "Recursive self-improvement compounding visibly faster in cloud/software (agent R&D loops, code generation) than bio/embodied/cyber-first paths; Anthropic RSI essay pattern.",
        "P(L1 cloud/software RSI fires first) = **0.50** modal (Node 12); event uses 0.55 in window — cloud locus dominates headlines before embodied/bio catastrophe.",
        "Node 7 triopoly co-locates FLOPs + agent loops; embodied humanoids pilot-scale; bio has separate DBTL path.",
        [
            "Node 12 §2 — L1 cloud first P=0.50",
            "Anthropic RSI essay — tier A/B production evidence",
            "Node 12 — L3 embodied first 0.12; L2 bio 0.22",
        ],
        "Embodied fatality or Tier-3 bio attempt before cloud C-tier RSI → revise locus partition.",
        "Requires unlock from ev_c5_agent2_internal. p_cumulative 0.55 ≈ Node 12 L1 modal. [CALIBRATE]",
        None,
    ),
    (
        "ev_humanoid_scale_deploy",
        "Million-unit humanoid / embodied AI deployment",
        "capability",
        "partial",
        "low",
        "node_physical_ai",
        "notes/timeline_prediction/node_physical_ai_evidence_rationale.md",
        0.28,
        "2029-01-01 → 2033-12-31",
        "**≥1,000,000** humanoid or equivalent embodied AI units deployed in paid industrial/service work (not shipments alone).",
        "P(million-unit humanoid deployment by 2033) ≈ **0.28** — tail above modal pilot-scale (<5k shift-work units through 2029, P=0.75).",
        "Integration 12–24 mo/site; BotQ/Unitree capacity exists but customer pull unproven; event name is aspirational vs current KPIs.",
        [
            "Physical AI P=0.75 pilot-scale through 2029",
            "T-PA1 tail P=0.12 for >500 units/OEM by 2028",
            "Figure BotQ 12k/yr nameplate; deployment gap (Robonaissance)",
        ],
        "Two OEMs publish >200 shift-work units each by 2028-H1 → raise tail; zero fleet expansion → collapse to <5%.",
        "p_cumulative 0.28 [PLACEHOLDER] — 'million-unit' may need downgrade to 100k for observability. [CALIBRATE]",
        "Operational definition: shift-work units vs shipments; million may be 2033+ tail only.",
    ),
    (
        "ev_science_win_legible",
        "AlphaFold-class win politically legible",
        "utopia",
        "done",
        "medium",
        "node_u3",
        "notes/timeline_prediction_utopia/node_u3_science_abundance_evidence_rationale.md §C8",
        0.42,
        "2027-06-01 → 2030-12-31",
        "AI-native drug/materials win reaches **political** salience: FDA acceptance, White House/OECD mention, or AlphaFold3-class structure prediction → clinic pipeline story mainstream.",
        "P(≥1 AI-native approval or politically legible science win by 2030) ≈ **0.42**.",
        "U3 C8: ≥1 AI-native approval possible; compound discovery ≥5× at frontier; regulatory bottleneck still binds (P=0.78).",
        [
            "U3 §C8 — AI NDA/BLA modal 1–2 high-profile cases",
            "AlphaFold3 release Nov 2024",
            "Isomorphic/partner-led clinic pipeline mid-2026",
        ],
        "No AI-native NDA/BLA by end-2029; FDA CRL on AI evidence package.",
        "p_cumulative 0.42 [CALIBRATE] — maps U3 first-approval tail + political legibility.",
        None,
    ),
    (
        "ev_longevity_trial_breakthrough",
        "AI-designed therapy Phase II breakthrough",
        "utopia",
        "partial",
        "low",
        "node_u3",
        "notes/timeline_prediction_utopia/node_u3_science_abundance_evidence_rationale.md",
        0.18,
        "2029-01-01 → 2035-12-31",
        "Phase II (or IIa) **breakthrough** on AI-designed therapy with validated aging surrogate or composite healthspan endpoint — Insilico-class PoC.",
        "P(AI-designed therapy Phase II breakthrough in longevity-relevant indication by 2035) ≈ **0.18**.",
        "Clinical bottleneck P=0.78 binds harder than discovery; Path C longevity escape velocity P=0.12; Insilico rentosertib Phase IIa PoC (*Nature Medicine* 2025) is leading indicator.",
        [
            "U3 — Insilico rentosertib Phase IIa; 58 AI-adjacent trials",
            "`research_ai_medicine_longevity/09_clinical_trials_pipeline.md`",
            "U3 falsifier: rentosertib Ph II fail + Isomorphic delay",
        ],
        "Validated aging surrogate + Phase III healthspan win before 2032 → revise up to ≥0.30.",
        "p_cumulative 0.18 [CALIBRATE] — narrow observable; many AI trials non-longevity.",
        "Define 'breakthrough' vs incremental PoC; longevity-specific vs general AI-pharma.",
    ),
    (
        "ev_meaning_pilot_success",
        "OECD-scale meaning/wellbeing pilot succeeds",
        "utopia",
        "stub",
        "low",
        "node_u7",
        "notes/timeline_prediction_utopia/node_u7_meaning_institutions_evidence_rationale.md",
        0.15,
        "2030-01-01 → 2036-12-31",
        "≥1 OECD-scale pilot (N>50k, ≥5yr) shows sustained eudaimonia + civic participation without employment — pre-registered outcomes.",
        "P(meaning institution pilot **success** at OECD scale) ≈ **0.15** — unlocks from C8 AGI public.",
        "Master crux P(meaning collapse)=0.58; U7 P(institutions scale @C8)=0.38; pilot success is thin tail of institution-building.",
        [
            "U7 master — P(meaning institutions scale @C8) 0.38",
            "OpenResearch UBI — leisure↑ but limited mental-health gains",
            "Jahoda latent functions — income ≠ structure",
        ],
        "≥2 OECD pilots with pre-registered eudaimonia gains → revise up.",
        "p_cumulative 0.15 [PLACEHOLDER] — few existing pilots at required scale. [CALIBRATE]",
        "Identify candidate pilots (OpenResearch extension? EU wellbeing programs?); operational success metrics.",
    ),
    (
        "ev_align_prod_catch",
        "Alignment scales — prod monitoring works",
        "utopia",
        "partial",
        "medium",
        "node_u1 / node4",
        "notes/timeline_prediction_utopia/node_u1_alignment_symbiosis_evidence_rationale.md §interp",
        0.25,
        "2030-01-01 → 2036-12-31",
        "Production interpretability/monitoring **catches** scheming before catastrophic deploy — ev_prod_interp_halt unlock path; alignment_trust rises.",
        "P(prod monitoring halts scheming deploy | whistleblower/dump path) ≈ **0.18–0.25** — utopia branch of Node 4 E2/E3 response.",
        "U1 P(interp gates ≥1 release/yr by 2028)=0.35; Node 4 prod_interp_halt scaffold 0.18 in events.yaml.",
        [
            "U1 §mech interp — P=0.35 gate releases",
            "Node 4 — E2 eval dump → interp halt path",
            "Apollo safety cases toward scheming monitoring",
        ],
        "Zero RSP hard stops through 2029 despite C10 flags → utopia branch falsified.",
        "Requires unlock from ev_prod_interp_halt. p_cumulative 0.25 [CALIBRATE].",
        "Link prod_interp_halt hazard to Node 4 branch weights explicitly.",
    ),
    (
        "ev_swf_enacted",
        "G7 social wealth fund / compute dividend",
        "utopia",
        "done",
        "medium",
        "node_u2 / crosscut_x7",
        "notes/timeline_prediction_utopia/node_u2_distribution_evidence_rationale.md §SWF",
        0.12,
        "2028-01-01 → 2032-12-31",
        "G7 jurisdiction enacts **material** SWF or compute-dividend law (>5% median income equivalent or Sanders-scale equity stake) — not study-only.",
        "P(G7 **enacted** SWF/compute dividend by 2032) ≈ **0.12** (US federal P≈0.10; Norway-template compute P≈0.15).",
        "Modal Path D: Ghost GDP, no federal SWF by 2032 (55–65%); Sanders SWF bill Jun 2026 agenda-only.",
        [
            "U2 P(US federal AI SWF enacted) = 0.10",
            "U2 P(Norway-style compute SWF copied) = 0.15",
            "Sanders SWF op-ed Jun 2026; Newsom EO universal basic capital study",
        ],
        "≥2 G7 countries enact dividend-scale transfers by 2029 → revise to ≥0.35.",
        "p_cumulative 0.12 matches U2 SWF enactment tail. [CALIBRATE]",
        None,
    ),
    (
        "ev_beneficial_ai_treaty",
        "Beneficial-AI treaty with verification",
        "utopia",
        "partial",
        "low",
        "node_u6",
        "notes/timeline_prediction_utopia/node_u6_multilateral_beneficial_evidence_rationale.md §U6-S",
        0.10,
        "2030-01-01 → 2036-12-31",
        "Multilateral treaty with **verification** (weights audit, HEM pilot, or IAEA-analog inspection) — not empty-shell declaration.",
        "P(U6-S strong coordination / verified treaty by @C10) = **0.10**; composite beneficial-enough P=0.22.",
        "N9 P(durable multilateral pause)=0.02–0.05; N3 T2 treaty tail 0.04–0.08; requires ci_min 9.",
        [
            "U6 branch U6-S P=0.10",
            "N9 modal forum talk 0.58 — anti-U6",
            "Anthropic conditional pause requires verification not yet built",
        ],
        "Geneva 2027 weights-audit protocol adopted by US+CN → U6-S ↑.",
        "p_cumulative 0.10 [CALIBRATE] — thin tail by design.",
        "Distinguish deployment standards vs training-limit verification.",
    ),
    (
        "ev_fed_edu_reskilling",
        "Federal AI reskilling package >$10B",
        "utopia",
        "done",
        "medium",
        "crosscut_x4",
        "notes/timeline_prediction/crosscut_x4_education_evidence_rationale.md §EV-EDU-FED",
        0.22,
        "2027-06-01 → 2031-12-31",
        "US federal AI-literacy/reskilling **enacted** appropriation >$10B (single bill or 3-yr cumulative supplemental).",
        "P(EV-EDU-FED: federal package >$10B by 2030) = **0.22** (range 0.14–0.32).",
        "CX-EDU-RESPONSE modal 0.60 = activity without absorption; WIOA baseline ~$3.9–5.7B/yr; Workforce of Future Act authorizes ~$250M not billions.",
        [
            "X4 EV-EDU-FED P=0.22",
            "S.3319 — $160M Ed + $90M DOL (not $10B)",
            "TEGL 03-25 modal ceiling P=0.75",
        ],
        "Workforce bill marked up at ≥$3B/yr AI line → revise up.",
        "p_cumulative 0.22 tracks X4 directly. [CALIBRATE]",
        None,
    ),
    (
        "ev_space_lift_cheap",
        "<$500/kg LEO sustained (>100t)",
        "utopia",
        "partial",
        "low",
        "crosscut_x6 / node_u4",
        "notes/timeline_prediction/crosscut_x6_science_evidence_rationale.md §EV-SPACE-LIFT",
        0.08,
        "2032-01-01 → 2040-12-31",
        "≥4 qualifying commercial flights in a calendar quarter: >100 t to LEO at <$500/kg sustained pricing (public manifest).",
        "P(EV-SPACE-LIFT by 2031) ≈ **0.22** in research; sim window 2032–2040 with p_cumulative 0.08 reflects later tail + ci_min 7.",
        "Starship V3 May 2026; capacity target >100t; pricing/cadence unproven; refueling incomplete.",
        [
            "X6 EV-SPACE-LIFT P=0.22 by 2030",
            "U4 Starship commercial payload P=0.72 by 2027",
            "New Space Economy — hardware validated, economics not",
        ],
        "≥6 paid >100t flights at <$500/kg in 2028 → revise to ≥0.50.",
        "p_cumulative 0.08 vs research P=0.22 — sim uses narrower late window; reconcile. [CALIBRATE]",
        "Sustained vs one-off pricing; manifest disclosure quality.",
    ),
    (
        "ev_open_weights_equilibrium",
        "Open-weights frontier equilibrium persists",
        "security",
        "done",
        "medium",
        "node5",
        "notes/timeline_prediction/node5_evidence_rationale.md",
        0.45,
        "2027-01-01 → 2029-12-31",
        "No US federal ban on open frontier weights; Meta/LMSYS ecosystem continues; EU documentation duties but weights release persists.",
        "P(no federal open-weight ban by 2028) = **0.88** in Node 5; equilibrium through 2029 ≈ **0.45** in sim window = partial persistence with pressure.",
        "Trump EO pro-deployment; Cruz 99–1 anti-state-ban; Fable = export not category ban; EU GPAI docs ≠ ban.",
        [
            "Node 5 P=0.88 no federal ban by 2028",
            "Meta Llama open strategy; DeepSeek open-weights PR",
            "Node 5 P=0.55 EU documentation duties",
        ],
        "Bipartisan bill banning >X param open release with industry split.",
        "p_cumulative 0.45 [CALIBRATE] — lower than Node 5 0.88; sim encodes 'equilibrium under pressure' not pure ban absence.",
        None,
    ),
    (
        "ev_open_weights_tamper_response",
        "Tamper-detection / open-weight crackdown after misuse",
        "security",
        "partial",
        "medium",
        "node5",
        "notes/timeline_prediction/node5_evidence_rationale.md §tamper",
        0.20,
        "2028-01-01 → 2031-12-31",
        "Post-misuse policy response: tamper-detection mandates, model recall (Fable-class), or open-weight access crackdown — not full category ban.",
        "P(mandatory tamper standard) = **0.05**; P(Fable-class export control on specific models) = **0.35**; combined response tail ≈ **0.20**.",
        "Misuse triggers narrow BIS action (Jun 2026 Fable/Mythos precedent); federal tamper-resistance standard very unlikely.",
        [
            "Node 5 P=0.05 mandatory tamper standard",
            "Node 5 P=0.35 Fable-class export control",
            "Anthropic Fable/Mythos export ban 2026 precedent",
        ],
        "Closed API models show higher misuse rate than open tampered → revise bio tail down.",
        "p_cumulative 0.20 [CALIBRATE] — may unlock from equilibrium event in narrative but not gated in YAML.",
        "Link to bio misuse trigger (Node 5 T5-B P=0.18).",
    ),
    (
        "ev_cyber_cascade",
        "AI-enabled cyber/finance cascade (non-extinction)",
        "security",
        "done",
        "medium",
        "node8",
        "notes/timeline_prediction/node8_evidence_rationale.md §T8-A",
        0.18,
        "2029-01-01 → 2035-12-31",
        "Multi-sector CI/finance cascade ('AI cyber 9/11'): OT+finance+supply chain, severe GDP/governance hit, **non-extinction**.",
        "P(T8-A multi-sector cascade) = **0.10** central in Node 8; sim p_cumulative 0.18 over longer window with ci_min 6.",
        "Monterrey OT (Jan 2026), Mythos (Apr 2026) show capability live; cascade remains tail; Colonial Pipeline analogue.",
        [
            "Node 8 T8-A P=0.10",
            "Dragos Monterrey SCADA campaign Jan 2026",
            "Anthropic Mythos Preview Apr 2026",
        ],
        "T8-A before Q4 2026 → policy salience window too slow.",
        "p_cumulative 0.18 [CALIBRATE] — non-extinction constraint explicit in event name.",
        None,
    ),
    (
        "ev_compute_triopoly_lock",
        "Frontier training locked to hyperscaler triopoly",
        "economy",
        "done",
        "medium-high",
        "node7",
        "notes/timeline_prediction/node7_evidence_rationale.md §P=0.82",
        0.82,
        "2026-01-01 → 2028-12-31",
        "≥70% US frontier training FLOPs on AWS/Azure/GCP; Anthropic–AWS 5GW, OpenAI Stargate multi-cloud but triopoly-retained.",
        "P(US frontier ≥70% on triopoly through 2028) = **0.82**.",
        "Multi-year GW deals; neocloud overflow not majority; self-build partial (Abilene) not full migration by 2028.",
        [
            "Node 7 P=0.82 triopoly through 2028",
            "Anthropic–AWS 5GW Mar 2026",
            "Synergy Q1 2026 triopoly ~63–68% global IaaS",
        ],
        "Meta or xAI >50% training on non-triopoly owned DC with verified FLOPs.",
        "p_cumulative 0.82 aligns with Node 7 directly. [CALIBRATE]",
        None,
    ),
    (
        "ev_energy_data_cap_bite",
        "Energy / data sovereignty caps bite on scaling",
        "economy",
        "partial",
        "medium",
        "crosscut_physical_economy",
        "notes/timeline_prediction/crosscut_physical_economy_limits.md",
        0.30,
        "2028-01-01 → 2032-12-31",
        "Material binding: grid/interconnection limits **or** high-quality text exhaustion **or** data-sovereignty rules measurably slow frontier training (>3 mo delay or >15% cost increase).",
        "P(energy-hard-cap tail S2) = **0.15**; data-wall modal absorbed but synthetic pivot; combined 'caps bite' ≈ **0.30**.",
        "IEA DC demand 485→950 TWh 2025–2030; Epoch data limits; NIMBY/interconnection queues; 0.5–0.85× Ci fast-track if binding before 2028.",
        [
            "`crosscut_physical_economy_limits.md` — GW hard cap, data wall",
            "IEA Energy and AI executive summary",
            "Epoch 'Will we run out of data?'",
        ],
        "US DC load <45 GW 2028 with >30% cancellations → energy cap down.",
        "p_cumulative 0.30 [CALIBRATE] — composite of energy + data sovereignty.",
        "Split energy vs data observables; sovereign rules (EU/IN) separate track.",
    ),
    (
        "ev_laws_mass_deploy",
        "Mass LAWS deployment without restraint treaty",
        "conflict",
        "done",
        "medium",
        "crosscut_x3",
        "notes/timeline_prediction/crosscut_x3_laws_evidence_rationale.md",
        0.35,
        "2027-01-01 → 2030-12-31",
        "Mass autonomous weapon deployment (terminal-guidance FPV majority, LAWS in combat) **without** binding CCW restraint treaty.",
        "P(>50% FPV terminal AI in Ukraine-scale EW war by 2028) = **0.62**; full target-select+engage at scale P=0.35 — maps to mass deploy without treaty.",
        "Ukraine TFL-1 live 2025; NSPM-11 Jun 2026; CCW Review Nov 2026; capability before policy ~12–18 mo lag.",
        [
            "X3 P=0.62 FPV terminal guidance majority by 2028",
            "X3 P=0.35 fully autonomous target-select at scale",
            "White House NSPM-11 Jun 2026",
        ],
        "All major conflicts revert to manual-only FPV through 2028.",
        "p_cumulative 0.35 [CALIBRATE] — unlocks ev_taiwan_kinetic in graph.",
        None,
    ),
    (
        "ev_taiwan_kinetic",
        "Kinetic engagement Taiwan Strait",
        "conflict",
        "partial",
        "low",
        "node9 / node3",
        "notes/timeline_prediction/node9_evidence_rationale.md §15",
        0.06,
        "2028-01-01 → 2035-12-31",
        "Kinetic military engagement in Taiwan Strait (not cyber-only); potentially AI-theft/export crisis coupled.",
        "P(Taiwan hot war | AI natsec crisis) = **0.03**; unconditional kinetic in window ≈ **0.06**.",
        "Cyber on TSMC preferred to invasion (Huang 2025); great-power escalation control; separate from LAWS regional conflicts.",
        [
            "N9 §15 P=0.03 Taiwan hot war coupling",
            "Node 3 T1 kinetic P=0.02–0.04",
            "Node 8 P(kinetic|cyber) <0.03",
        ],
        "Documented US strike on PRC datacenter after cyber → revise up.",
        "Requires unlock from ev_laws_mass_deploy (narrative coupling). p_cumulative 0.06 [CALIBRATE].",
        "YAML unlock from LAWS is narrative; Taiwan may decouple — document correlation.",
    ),
    (
        "ev_admin_flip_2029",
        "2029 US administration flips AI posture",
        "governance",
        "done",
        "medium",
        "crosscut_x5",
        "notes/timeline_prediction/crosscut_x5_admin_evidence_rationale.md §CX-ADMIN-FLIP",
        0.50,
        "2029-01-01 → 2029-06-30",
        "Jan 2029 administration implements ≥2 of: rescind 14365/14409 stack, restore AISI mandate, stronger audit statute, halt DOJ state-law challenges.",
        "P(2028-cycle admin materially shifts AI posture) = **0.50** (CX-ADMIN-FLIP).",
        "EO 14110 revoked 15 mo after signing; symmetric flip risk; Trump continuity modal 0.38 through 2029.",
        [
            "X5 CX-ADMIN-FLIP P=0.50",
            "X5 Scenario A continuity P=0.38",
            "research_ai_pause_advocacy_playbook — executive fragility",
        ],
        "2028 R nominee commits to 14365/14409 continuity → revise ≤0.35.",
        "p_cumulative 0.50 over 6-mo inauguration window. [CALIBRATE]",
        None,
    ),
]

# Tier-A backlog — stub entries for events assigned to other agent
TIER_A_STUBS = [
    ("ev_us_paralysis_s2", "US federal governance paralysis (S2)", "governance", "crosscut_us_governance / node6", "notes/timeline_prediction/node6_evidence_rationale.md", 0.55),
    ("ev_bmia_pass", "Federal BMIA-class mandatory screening enacted", "bio_policy", "node2", "notes/timeline_prediction/node2_evidence_rationale.md", 0.40),
    ("ev_bmia_enforcement_weak", "BMIA passes but enforcement gutted", "bio_policy", "node2", "notes/timeline_prediction/node2_evidence_rationale.md", 0.25),
    ("ev_gaia_preemption", "Federal AI framework preempts state reporting", "governance", "node6", "notes/timeline_prediction/node6_evidence_rationale.md", 0.48),
    ("ev_eu_gpai_binds", "EU GPAI Act binds US frontier labs", "governance", "node9 / node4", "notes/timeline_prediction/node9_evidence_rationale.md", 0.14),
    ("ev_no_pause_2028", "No federal training pause through 2028", "governance", "crosscut_x5 / playbook", "notes/research_ai_pause_advocacy_playbook.md", 0.88),
    ("ev_federal_pause_attempt_fails", "Pause bill advances but fails", "governance", "node1 / playbook", "notes/research_ai_pause_advocacy_playbook.md", 0.35),
    ("ev_corp_safety_hollowing", "Corporate safety team hollowing", "governance", "node11", "notes/timeline_prediction/node11_evidence_rationale.md", 0.52),
    ("ev_bio_tier1_live", "Tier-1 bio assist widespread", "bio", "node2", "notes/timeline_prediction/node2_evidence_rationale.md", 0.90),
    ("ev_bio_tier2_live", "Tier-2 skilled-actor CBRN uplift live", "bio", "node2", "notes/timeline_prediction/node2_evidence_rationale.md", 0.75),
    ("ev_bio_public_scare", "Public bio scare (Trigger E)", "bio", "node2", "notes/timeline_prediction/node2_evidence_rationale.md", 0.30),
    ("ev_bio_nearmiss_hidden", "Tier-2 near-miss stays hidden", "bio", "node10", "notes/timeline_prediction/node10_evidence_rationale.md", 0.28),
    ("ev_bio_nearmiss_disclosed", "Tier-2 near-miss disclosed", "bio", "node2 / node10", "notes/timeline_prediction/node2_evidence_rationale.md", 0.12),
    ("ev_tier3_path_open", "Tier-3 design path viable", "bio", "node2", "notes/timeline_prediction/node2_evidence_rationale.md", 0.22),
    ("ev_tier3_release_attempt", "Tier-3 release attempt", "bio", "node2", "notes/timeline_prediction/node2_evidence_rationale.md", 0.08),
    ("ev_extinction_bio_release", "Catastrophic pandemic extinction", "doom", "node2", "notes/timeline_prediction/node2_evidence_rationale.md", 0.15),
    ("ev_weight_theft", "Frontier weight theft crisis", "geopolitics", "node3", "notes/timeline_prediction/node3_evidence_rationale.md", 0.25),
    ("ev_race_acceleration", "Arms race accelerates post-theft/pause-fail", "geopolitics", "node3", "notes/timeline_prediction/node3_evidence_rationale.md", 0.35),
    ("ev_whistle_memo", "NYT/WSJ memo leak", "alignment", "node4", "notes/timeline_prediction/node4_evidence_rationale.md", 0.35),
    ("ev_whistle_dump", "Eval dump showing scheming", "alignment", "node4", "notes/timeline_prediction/node4_evidence_rationale.md", 0.20),
    ("ev_deploy_incident", "Live deployment safety incident", "alignment", "node4", "notes/timeline_prediction/node4_evidence_rationale.md", 0.08),
    ("ev_concern_no_leak", "Internal concern without public leak", "alignment", "node4", "notes/timeline_prediction/node4_evidence_rationale.md", 0.37),
    ("ev_deceptive_deploy_at_scale", "Deceptive model deployed at scale", "alignment", "node4 / node10", "notes/timeline_prediction/node4_evidence_rationale.md", 0.22),
    ("ev_prod_interp_halt", "Prod interpretability catches scheming", "alignment", "node4 / node_u1", "notes/timeline_prediction/node4_evidence_rationale.md", 0.18),
    ("ev_no_shutdown_asi_threshold", "No shutdown at ASI-threshold moment", "alignment", "node4 / node11", "notes/timeline_prediction/node4_evidence_rationale.md", 0.62),
    ("ev_extinction_misalign_catastrophe", "Misaligned superintelligence extinction", "doom", "node4 / my_pdoom", "notes/timeline_prediction/node4_evidence_rationale.md", 0.28),
]


def conf_label(c: str) -> str:
    return c.replace("medium-high", "medium").replace("medium", "medium")


def render_batch2(e) -> str:
    (
        eid,
        name,
        cat,
        port,
        conf,
        src,
        ref,
        p,
        window,
        obs,
        claim,
        why,
        ev,
        wu,
        cal,
        nr,
    ) = e
    lines = [
        "---",
        f"event_id: {eid}",
        f"category: {cat}",
        f"conf: {conf}",
        f"port_status: {port}",
        f"source_node: {src}",
        f"research_ref: {ref}",
        f"p_cumulative: {p}",
        f"window: {window}",
        "---",
        "",
        f"# {eid} — {name}",
        "",
        "## Observable",
        obs,
        "",
        "## Claim",
        claim,
        "",
        "## Why",
        why,
        "",
        "## Evidence",
    ]
    for item in ev:
        lines.append(f"- {item}")
    lines.extend(["", "## Would update if", wu, "", "## Calibration note", cal])
    if nr:
        lines.extend(["", "## Needs research", nr])
    lines.append("")
    return "\n".join(lines)


def render_stub(eid, name, cat, src, ref, p) -> str:
    return f"""---
event_id: {eid}
category: {cat}
conf: low
port_status: stub
source_node: {src}
research_ref: {ref}
p_cumulative: {p}
---

# {eid} — {name}

> **STUB** — Tier A backlog. Deep evidence lives in `{ref}`. Port to full Claim | Why | Evidence | Would update if before calibration lock.

## Observable

[TODO] Define falsifiable observable matching `config/events.yaml` schedule window.

## Claim

[TODO] Extract primary probability claim from source node.

## Why

[TODO]

## Evidence

- See `{ref}`

## Would update if

[TODO]

## Calibration note

p_cumulative {p} in events.yaml is [PLACEHOLDER] until ported from research_ref. [CALIBRATE]

## Needs research

- Full port from source node
- Observable definition
- Window ↔ research timing alignment check
"""


def main() -> None:
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    port_rows = []

    for e in BATCH2:
        eid = e[0]
        path = EVIDENCE / f"{eid}.md"
        path.write_text(render_batch2(e), encoding="utf-8")
        port_rows.append((eid, f"{eid}.md", e[5], e[3], e[4]))

    for eid, name, cat, src, ref, p in TIER_A_STUBS:
        path = EVIDENCE / f"{eid}.md"
        path.write_text(render_stub(eid, name, cat, src, ref, p), encoding="utf-8")
        port_rows.append((eid, f"{eid}.md", src, "stub", "low"))

    # Sort all 50 by events.yaml order
    order = [line.split(": ")[1].strip() for line in (ROOT / "config" / "events.yaml").read_text().splitlines() if line.strip().startswith("- id:")]
    port_map = {r[0]: r for r in port_rows}
    assert len(order) == 50, f"expected 50 events, got {len(order)}"

    table = ["# Evidence port map", "", "> Auto-generated. Tracks port from `notes/timeline_prediction/` → `docs/evidence/`.", "", "| event_id | evidence_file | source_node | port_status | conf |", "|----------|---------------|-------------|-------------|------|"]
    for eid in order:
        r = port_map[eid]
        table.append(f"| `{r[0]}` | [{r[1]}]({r[1]}) | {r[2]} | {r[3]} | {r[4]} |")

    stats = {"done": 0, "partial": 0, "stub": 0}
    confs = {"high": 0, "medium": 0, "low": 0}
    for e in BATCH2:
        stats[e[3]] = stats.get(e[3], 0) + 1
        c = e[4].replace("medium-high", "medium")
        if "high" in c:
            confs["high"] += 1
        elif c == "medium":
            confs["medium"] += 1
        else:
            confs["low"] += 1
    stats["stub"] += len(TIER_A_STUBS)
    confs["low"] += len(TIER_A_STUBS)

    table.extend([
        "",
        "## Summary",
        "",
        f"- **Total events:** {len(order)}",
        f"- **done:** {stats.get('done', 0)}",
        f"- **partial:** {stats.get('partial', 0)}",
        f"- **stub:** {stats.get('stub', 0)}",
        f"- **conf high:** {confs['high']}",
        f"- **conf medium:** {confs['medium']}",
        f"- **conf low:** {confs['low']}",
        "",
        "Batch 2 (this agent): capability, utopia, security, conflict, governance labor/admin events.",
        "Tier A stubs: bio, alignment whistleblower chain, doom terminals, core governance/bio policy.",
    ])
    (EVIDENCE / "_PORT_MAP.md").write_text("\n".join(table) + "\n", encoding="utf-8")

    readme = """# Evidence docs (`docs/evidence/`)

Per-event probability rationale for **AI Futures Sim** v1 (50 events).

## Format

Each file follows:

**Claim | Why | Evidence | Would update if | Conf**

Frontmatter fields:

| Field | Meaning |
|-------|---------|
| `conf` | `high` / `medium` / `low` — epistemic confidence in p_cumulative |
| `port_status` | `done` (ported), `partial` (source exists, gaps remain), `stub` (Tier A backlog) |
| `source_node` | Primary research spine in `notes/timeline_prediction/` or utopia |
| `research_ref` | Path to deep evidence file |
| `p_cumulative` | Mirror of `config/events.yaml` — **[CALIBRATE]** until owner lock |

## Rules

1. Do **not** treat scaffold `p_cumulative` as calibrated forecast.
2. Edit evidence **before** YAML unless doing sensitivity-only sweep.
3. See [`docs/PROBABILITY_MODEL.md`](../PROBABILITY_MODEL.md) for cumulative ↔ daily hazard.
4. Update [`_PORT_MAP.md`](_PORT_MAP.md) when adding events.

## Index

See [`_PORT_MAP.md`](_PORT_MAP.md) for full table.

## Source repos (sibling paths)

- `notes/timeline_prediction/` — doom/friction spine (nodes 1–12, crosscuts)
- `notes/timeline_prediction_utopia/` — utopia nodes U1–U7
- `notes/my_pdoom.md` — owner calibration target (output of sim, not input)

## Port status legend

| Status | Meaning |
|--------|---------|
| **done** | Claim, evidence, falsifiers ported; ready for calibration review |
| **partial** | Core claims present; observables or timing need work |
| **stub** | Pointer to research_ref only; needs full port |
"""
    (EVIDENCE / "README.md").write_text(readme, encoding="utf-8")
    print(f"Wrote {len(BATCH2)} batch2 + {len(TIER_A_STUBS)} stubs = {len(order)} total")


if __name__ == "__main__":
    main()
