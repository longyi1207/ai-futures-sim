/** Branching timeline — Sankey-style ribbons from export_branching_timeline.py */

const BT_REGION_COLORS = {
  doom: "#f28b82",
  utopia: "#81c995",
  friction: "#fdd663",
  severe: "#c58af9",
};

function btPct(x) {
  return `${(100 * x).toFixed(1)}%`;
}

function btLinkColor(fromId, toId, nodesById) {
  const to = nodesById[toId];
  if (to?.region) return BT_REGION_COLORS[to.region] || "#7baaf7";
  if (toId.includes("pause")) return "#f4a261";
  if (toId.includes("race")) return "#e76f51";
  if (toId.includes("c10")) return "#c58af9";
  if (toId.includes("spine") || fromId === "start") return "#7baaf7";
  return "#5c8df6";
}

function btLayoutNodes(nodes, width, height, colCount) {
  const padX = 100;
  const padY = 36;
  const colW = (width - padX * 2) / (colCount - 1);
  const byCol = new Map();
  for (const n of nodes) {
    if (!byCol.has(n.col)) byCol.set(n.col, []);
    byCol.get(n.col).push(n);
  }

  const positioned = new Map();
  for (const [col, list] of byCol.entries()) {
    const sorted = [...list].sort((a, b) => b.share - a.share);
    const totalH = height - padY * 2;
    let y = padY;
    const gap = 10;
    const sumShare = sorted.reduce((s, n) => s + n.share, 0);
    for (const n of sorted) {
      const h = Math.max(18, (n.share / sumShare) * totalH - gap);
      positioned.set(n.id, {
        ...n,
        x: padX + col * colW,
        y,
        w: 18,
        h,
      });
      y += h + gap;
    }
  }
  return positioned;
}

function btRibbonPath(x0, y0, h0, x1, y1, h1) {
  const mx = (x0 + x1) / 2;
  return [
    `M ${x0 + 18} ${y0}`,
    `C ${mx} ${y0}, ${mx} ${y1}, ${x1} ${y1}`,
    `L ${x1} ${y1 + h1}`,
    `C ${mx} ${y1 + h1}, ${mx} ${y0 + h0}, ${x0 + 18} ${y0 + h0}`,
    "Z",
  ].join(" ");
}

function renderBranchingTimeline(container, data) {
  if (!data?.nodes?.length) {
    container.innerHTML =
      "<p class='muted'>No branching data — run <code>python scripts/export_branching_timeline.py</code></p>";
    return;
  }

  const width = Math.min(1100, container.clientWidth || 1100);
  const height = 420;
  const nodesById = Object.fromEntries(data.nodes.map((n) => [n.id, n]));
  const positioned = btLayoutNodes(data.nodes, width, height, data.columns.length);

  const outOffset = new Map();
  const inOffset = new Map();
  for (const id of positioned.keys()) {
    outOffset.set(id, 0);
    inOffset.set(id, 0);
  }

  const links = [...data.links].sort((a, b) => a.from.localeCompare(b.from));
  const ribbons = [];

  for (const link of links) {
    const from = positioned.get(link.from);
    const to = positioned.get(link.to);
    if (!from || !to) continue;

    const lh = Math.max(2, from.h * (link.share / from.share));
    const rh = Math.max(2, to.h * (link.share / to.share));

    const y0 = from.y + outOffset.get(link.from);
    const y1 = to.y + inOffset.get(link.to);
    outOffset.set(link.from, outOffset.get(link.from) + lh);
    inOffset.set(link.to, inOffset.get(link.to) + rh);

    ribbons.push({
      d: btRibbonPath(from.x, y0, lh, to.x, y1, rh),
      color: btLinkColor(link.from, link.to, nodesById),
      opacity: Math.min(0.55, 0.2 + link.share * 2),
      title: `${nodesById[link.from]?.label || link.from} → ${nodesById[link.to]?.label || link.to}: ${btPct(link.share)}`,
    });
  }

  const colLabels = data.columns
    .map(
      (c) => `
    <text x="${100 + c.id * ((width - 200) / (data.columns.length - 1))}" y="22"
      text-anchor="middle" class="bt-col-year">${c.year}</text>
    <text x="${100 + c.id * ((width - 200) / (data.columns.length - 1))}" y="38"
      text-anchor="middle" class="bt-col-label">${c.label}</text>`
    )
    .join("");

  const nodeEls = [...positioned.values()]
    .map((n) => {
      const fill = n.region ? BT_REGION_COLORS[n.region] : "#7baaf7";
      return `<g class="bt-node" data-id="${n.id}">
        <rect x="${n.x}" y="${n.y}" width="${n.w}" height="${n.h}" rx="4" fill="${fill}" opacity="0.92"/>
        <text x="${n.x + n.w + 8}" y="${n.y + 14}" class="bt-node-label">${n.label}</text>
        <text x="${n.x + n.w + 8}" y="${n.y + 28}" class="bt-node-pct">${btPct(n.share)}</text>
      </g>`;
    })
    .join("");

  const ribbonEls = ribbons
    .map(
      (r) =>
        `<path d="${r.d}" fill="${r.color}" fill-opacity="${r.opacity}" stroke="none"><title>${r.title}</title></path>`
    )
    .join("");

  const topPaths = (data.top_paths || [])
    .slice(0, 5)
    .map(
      (p) =>
        `<li><span class="bt-path-region ${p.region}">${p.region}</span> ${btPct(p.share)} — ${p.labels.join(" → ")}</li>`
    )
    .join("");

  container.innerHTML = `
    <div class="bt-header">
      <p class="section-hint">${data.meta?.subtitle || ""}</p>
      <div class="bt-legend">
        <span class="bt-legend-title">Colors</span>
        <span><i class="swatch swatch-spine"></i> Capability stage (not an outcome)</span>
        <span><i class="swatch swatch-gov"></i> Governance fork (race / paralysis / pause)</span>
        <span><i class="swatch swatch-c10"></i> C10 alignment scare branch</span>
        <span><i class="swatch swatch-friction"></i> Friction</span>
        <span><i class="swatch swatch-doom"></i> Doom</span>
        <span><i class="swatch swatch-utopia"></i> Utopia</span>
        <span><i class="swatch swatch-severe"></i> Severe</span>
      </div>
    </div>
    <svg class="bt-svg" viewBox="0 0 ${width} ${height}" width="100%" aria-label="Branching futures timeline">
      ${colLabels}
      ${ribbonEls}
      ${nodeEls}
    </svg>
    <div class="bt-footer">
      <div class="bt-top-paths">
        <h3>Modal story paths</h3>
        <ul>${topPaths}</ul>
      </div>
      <div class="bt-buckets">
        <h3>Named path buckets</h3>
        ${Object.entries(data.path_buckets || {})
          .sort((a, b) => b[1] - a[1])
          .slice(0, 5)
          .map(([k, v]) => `<div class="bt-bucket"><span>${k.replace(/_/g, " ")}</span><span>${btPct(v)}</span></div>`)
          .join("")}
      </div>
    </div>`;
}
