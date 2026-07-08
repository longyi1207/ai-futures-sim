# Research sources (OSS port)

Evidence files in `docs/evidence/` cite **deep rationale** documents. In the private monorepo those live in a separate `notes` tree; this folder is the **public, self-contained mirror** for open-source readers.

## Recommendation: selective copy, not inline everything

| Approach | Verdict |
|----------|---------|
| Copy entire private notes tree | **No** — career notes, Chinese-only primers, unrelated research, ~MB of noise |
| Inline all source text into 58 evidence files | **No** — `node2_evidence_rationale.md` alone is 1000+ lines cited by 15+ events; unmaintainable duplication |
| **Selective copy into `docs/research/` + thin evidence summaries** | **Yes** |

### Three layers

```
docs/evidence/ev_foo.md     ← reader-facing: Observable, Claim, Why, YAML mapping (~60 lines)
docs/research/spine/...     ← ported deep rationale (one file, many events cite it)
docs/research/supplements/  ← one-off primers, tracker, methodology excerpts
```

**Evidence stays the index.** Research files hold load-bearing P's, branch tables, and falsifiers. A reader can trace any `p_cumulative` in two hops.

## What to copy

See [`MANIFEST.md`](MANIFEST.md) — **~48 English files** actually cited by evidence (as of 2026-07-07). Includes:

- `timeline_prediction/*_evidence_rationale.md` + crosscuts + `c8_society_snapshot_by_ci.md`
- `timeline_prediction_utopia/node_u*.md` (5 files)
- `ai_futures_archive_2026-07/` — `03_ci_spine.md`, `05_crux_registry.md`, `08_parallel_spines.md` only
- Supplements: pause playbook, tracker scorecard, `timeline_prediction_node2_cbrn_full.md`

## What NOT to copy (inline excerpt instead)

| Private source | OSS handling |
|----------------|--------------|
| Personal P(doom) calibration | [`supplements/pdoom_methodology.md`](supplements/pdoom_methodology.md) — Adelstein/Hanson defs only |
| Chinese primers / 深度解读 | English claims + primary URLs in evidence |
| Private event chronicles | Facts already in evidence; external URLs |
| Retired events registry | `config/events.yaml` is canonical |

## Link hygiene policy

**Goal:** OSS readers never need the private monorepo to follow in-repo citations.

| Rule | Detail |
|------|--------|
| **Internal links** | Use **relative** paths within `docs/research/` (e.g. `[node2](../spine/node2_evidence_rationale.md)` from `utopia/`) |
| **Ported headers** | Keep one-line `> **Ported from:**` with original private path — the only intentional `notes/` substring in research files |
| **Private-only sources** | Replace with public URL, [`supplements/pdoom_methodology.md`](supplements/pdoom_methodology.md), or `<!-- private monorepo only -->` on the bullet |
| **Rewrite tooling** | `python scripts/port_research_refs.py --rewrite-research-links` after re-port |
| **CI check** | `python scripts/port_research_refs.py --check` validates evidence → research resolution |

**Mapping (private → OSS):**

| Private prefix | OSS folder |
|----------------|------------|
| `timeline_prediction/` | `spine/` |
| `timeline_prediction_utopia/` | `utopia/` |
| `ai_futures_archive_2026-07/`, `ai_futures/` | `reference/` |
| One-off primers | `supplements/` |

## Port workflow

From monorepo root (private):

```bash
cd ai_futures_sim
python scripts/port_research_refs.py --copy              # copies MANIFEST files from private notes root
python scripts/port_research_refs.py --rewrite-research-links  # fix internal links in docs/research/
python scripts/port_research_refs.py --check               # fails CI if evidence cites missing in-repo paths
python scripts/port_research_refs.py --rewrite-links       # evidence/config one-time (already done)
```

Each copied file gets a header:

```markdown
> **Ported from:** `timeline_prediction/node2_evidence_rationale.md` · snapshot YYYY-MM-DD · edit canonical copy in private monorepo until OSS lock
```

## Link convention (after port)

| Before (private) | After (OSS, relative from spine/) |
|------------------|-----------------------------------|
| `timeline_prediction/node2_evidence_rationale.md` | `node2_evidence_rationale.md` |
| `timeline_prediction_utopia/node_u7_...` | `../utopia/node_u7_...` |
| `ai_futures_archive_2026-07/05_crux_registry.md` | `../reference/05_crux_registry.md` |

`research_ref` in `config/events.yaml` should point at `docs/research/...` before public release.

## Maintenance

- **Private monorepo:** continue editing `timeline_prediction/` as canonical until you declare OSS lock.
- **Re-port:** run `--copy` then `--rewrite-research-links` before tagged releases; diff `docs/research/` in release notes.
- **New event:** add evidence file + ensure cited research file is in MANIFEST (or add excerpt).
