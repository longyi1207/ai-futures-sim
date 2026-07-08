# P(doom) methodology excerpt (OSS)

> **Ported from:** private monorepo `my_pdoom.md` · methodology only — **no personal headline calibration**. Sim output is TBD after calibration lock.

## Definitions

| Bucket | Framing |
|--------|---------|
| **Extinction** | Human extinction by ~2050 |
| **Permanent agency loss** | Humans exist but lose durable control ("whimper") |
| **Severe but recoverable** | >$10T damage, no extinction |
| **Concentrated harm** | Surveillance, inequality — not macro x-risk |

Always state: `P(___ by ___ from ___ mechanism)`.

## Synthesis methods

**Adelstein conjunction (low-doom decomposition):**

```
P(extinction) ≈ P(¬default_align) × P(fail|effort) × P(no_shutdown) × P(no_coord) × …
```

**Hanson disjunction (multi-scenario — watch double-counting):**

```
P(bad) ≈ P(misaligned SI) + P(AI bio) + P(AI war) + P(whimper)
```

## Load-bearing cruxes (see also `docs/research/reference/05_crux_registry.md`)

| Crux | Typical range | Sim events |
|------|---------------|------------|
| CX-NO-PAUSE | 0.83–0.93 | `ev_no_pause_2028` |
| CX-DECEPTION | 0.55–0.85 | `ev_deceptive_deploy_at_scale` |
| P(no_shutdown \| crisis) | 0.12–0.18 | `ev_no_shutdown_asi_threshold` |
| Bio extinction (MODAL) | ~1–3% of total mass | `ev_extinction_bio_release` chain |
| Misalign extinction \| C10 modal | 12–22% mid ~17% | `ev_extinction_misalign_catastrophe` |

## Retired (do not use)

Three-branch mixture (modal/bio/misalign RPG branches) — **method error**. Real world is one joint timeline; use event-graph sim instead.

## External references

<!-- private monorepo only: - Adelstein conjunction decomposition — see `<!-- private monorepo only -->` S1 (private monorepo; English: alignment debate summaries) -->- Crux registry: `docs/research/reference/05_crux_registry.md`
