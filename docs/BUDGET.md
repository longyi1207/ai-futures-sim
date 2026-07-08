# Budget ledger — AI Futures Sim

**Cap:** $200 USD (owner-approved 2026-07-07)  
**Spent:** $0.00  
**Remaining:** $200.00  

Update this file **every time** paid API or cloud resources are used.

---

## Policy (summary)

| Rule | Detail |
|------|--------|
| Justified use OK | LLM API, cloud compute when efficiency/accuracy warrants it |
| Ask before >$20 | Single line-item estimate in this file first |
| Warn at $150 | Cumulative spend; confirm with owner before more |
| Local first | 10k sims on M4; don't cloud what runs in <1 hr locally |
| Secrets | LLM Vault only; never commit keys |

See [`CLAUDE.md`](../CLAUDE.md) § Budget & external resources.

---

## Spend log

| Date | Vendor | Purpose | Amount (USD) | Running total | Notes |
|------|--------|---------|--------------|---------------|-------|
| — | — | *(no spend yet)* | — | **$0.00** | Scaffold built locally |

---

## Planned / estimated (not spent)

| Item | Est. cost | When | Status |
|------|-----------|------|--------|
| Batch LLM evidence port (50 events × ~2k tokens) | ~$5–15 | Calibration phase | not started |
| Cloud GPU (only if ensemble >>10k runs) | ~$10–50 | Optional | not started |
| Vercel/static hosting for `web/` | ~$0–20 | Viz phase | not started |

---

## How to log a new entry

```markdown
| 2026-XX-XX | OpenAI / AWS / … | Short purpose | 12.34 | 12.34 | model, ~Nk tokens or instance type |
```

Then update **Spent** and **Remaining** at the top.
