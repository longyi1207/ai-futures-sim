#!/usr/bin/env bash
# Regenerate the Mermaid-sourced report figures (Fig. 4, Fig. 5) from
# docs/diagrams/*.mmd. Requires Node (npx pulls @mermaid-js/mermaid-cli on
# first run). Source diagrams are the reproducible artifact; the PNGs in
# docs/figures/ are the committed, embeddable output.
set -euo pipefail
cd "$(dirname "$0")/.."

npx --yes @mermaid-js/mermaid-cli \
  -i docs/diagrams/daily_loop_main.mmd \
  -o docs/figures/fig4_daily_loop.png \
  -w 2000 --backgroundColor white

npx --yes @mermaid-js/mermaid-cli \
  -i docs/diagrams/daily_loop_step4.mmd \
  -o docs/figures/fig5_step4_detail.png \
  -w 1800 --backgroundColor white

echo "wrote docs/figures/fig4_daily_loop.png"
echo "wrote docs/figures/fig5_step4_detail.png"
