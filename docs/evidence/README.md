# Evidence docs (`docs/evidence/`)

Per-event and **spine milestone** probability rationale for **AI Futures Sim** (57 events + 7 spine milestones).

## Format

Each file follows:

**Claim | Why | Evidence | Would update if | Conf**

Frontmatter fields:

| Field | Meaning |
|-------|---------|
| `conf` | `high` / `medium` / `low` — epistemic confidence in p_cumulative |
| `port_status` | `done` / `partial` — depth of port |
| `source_node` | Primary research spine |
| `research_ref` | Path to deep evidence — **`docs/research/...`** after OSS port |
| `p_cumulative` | Mirror of `config/events.yaml` or `config/spine.yaml` — **[CALIBRATE]** until owner lock |
| `milestone_id` | Spine only (`sp_c*`) |
| `status: superseded` | Event migrated to spine — follow `redirect` |

## Spine vs events

| Layer | Config | Evidence prefix |
|-------|--------|-----------------|
| AI-2027 capability | `config/spine.yaml` | `sp_c*.md` |
| Plot beats | `config/events.yaml` | `ev_*.md` |

C3/C4/C10 plot beats are **events only**. C5/C6/C8 capability → **spine** (`ev_c5/c6/c8` evidence files are redirect stubs).

## Rules

1. Do **not** treat scaffold `p_cumulative` as calibrated forecast.
2. Edit evidence **before** YAML unless doing sensitivity-only sweep.
3. See [`docs/PROBABILITY_MODEL.md`](../PROBABILITY_MODEL.md) for cumulative ↔ daily hazard.
4. Update [`_PORT_MAP.md`](_PORT_MAP.md) when adding events.

## Index

See [`_PORT_MAP.md`](_PORT_MAP.md) for full table.

## Research sources (OSS)

Deep rationale lives in [`docs/research/`](../research/) — ported selectively from private `notes/`. See [`docs/research/README.md`](../research/README.md) for port policy.

```bash
python scripts/port_research_refs.py --copy    # snapshot from ../notes/
python scripts/port_research_refs.py --check   # CI: all refs resolve
```

**OSS:** All `research_ref` paths use `docs/research/` (run `python3 scripts/port_research_refs.py --copy` before release).

## Port status legend

| Status | Meaning |
|--------|---------|
| **done** | Claim, evidence, falsifiers ported; ready for calibration review |
| **partial** | Core claims present; observables or timing need work |
