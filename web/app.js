const REGION_COLORS = {
  doom: "#f28b82",
  utopia: "#81c995",
  friction: "#fdd663",
  severe: "#c58af9",
};

const REGION_ORDER = ["doom", "utopia", "friction", "severe"];

function pct(x) {
  return `${(100 * x).toFixed(1)}%`;
}

function bar(label, value, cls = "") {
  const w = Math.min(100, 100 * value);
  return `<div class="bar-row">
    <div class="bar-label"><span>${label}</span><span>${pct(value)}</span></div>
    <div class="bar-track"><div class="bar-fill ${cls}" style="width:${w}%"></div></div>
  </div>`;
}

function drawDonut(regions) {
  const canvas = document.getElementById("donut");
  const ctx = canvas.getContext("2d");
  const cx = canvas.width / 2;
  const cy = canvas.height / 2;
  const r = 88;
  const inner = 52;
  let start = -Math.PI / 2;
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  for (const key of REGION_ORDER) {
    const v = regions[key] || 0;
    if (v <= 0) continue;
    const angle = v * 2 * Math.PI;
    ctx.beginPath();
    ctx.arc(cx, cy, r, start, start + angle);
    ctx.arc(cx, cy, inner, start + angle, start, true);
    ctx.closePath();
    ctx.fillStyle = REGION_COLORS[key];
    ctx.fill();
    start += angle;
  }

  ctx.fillStyle = "#e8eaed";
  ctx.font = "600 13px system-ui";
  ctx.textAlign = "center";
  ctx.fillText("emergent", cx, cy - 4);
  ctx.fillStyle = "#9aa0a6";
  ctx.font = "11px system-ui";
  ctx.fillText("regions", cx, cy + 12);
}

function renderRegions(regions) {
  drawDonut(regions);
  let html = "";
  for (const k of REGION_ORDER) {
    html += bar(k, regions[k] || 0, k);
  }
  document.getElementById("region-bars").innerHTML = html;
}

function renderMeta(cal, path) {
  const runs = cal?.runs || path?.runs || "—";
  const seed = cal?.seed ?? path?.seed ?? "—";
  document.getElementById("meta").innerHTML = `
    <h2>Run meta</h2>
    <table>
      <tr><th>Runs</th><td>${runs}</td></tr>
      <tr><th>Seed</th><td>${seed}</td></tr>
      <tr><th>Early absorb</th><td>${cal?.early_absorb_rate != null ? pct(cal.early_absorb_rate) : "—"}</td></tr>
      <tr><th>Horizon assign</th><td>${cal?.horizon_absorb_rate != null ? pct(cal.horizon_absorb_rate) : "—"}</td></tr>
      <tr><th>Full spine c1→c9</th><td>${cal?.path_buckets?.full_spine != null ? pct(cal.path_buckets.full_spine) : "—"}</td></tr>
    </table>`;
}

function renderSpineCourse(cal) {
  const el = document.getElementById("spine-timeline");
  const med = cal?.spine_median_day || {};
  const byDeadline = cal?.spine_by_deadline || {};
  const milestones = Object.keys(med).sort((a, b) => {
    const da = med[a] || "9999";
    const db = med[b] || "9999";
    return da.localeCompare(db);
  });

  if (!milestones.length) {
    el.innerHTML = "<p class='muted'>No spine median data — load calibration_summary.json</p>";
    return;
  }

  const start = new Date("2026-01-01");
  const end = new Date("2032-01-01");
  const span = end - start;

  let nodes = "";
  for (const mid of milestones) {
    const dateStr = med[mid];
    if (!dateStr) continue;
    const d = new Date(dateStr);
    const frac = Math.max(0, Math.min(1, (d - start) / span));
    const left = `${(frac * 100).toFixed(1)}%`;
    const p = byDeadline[mid] ?? 0;
    const label = mid.replace("sp_", "C");
    nodes += `<div class="spine-node" style="left:${left}">
      <div class="spine-label">${label}</div>
      <div class="spine-dot"></div>
      <div class="spine-date">${dateStr.slice(0, 7)}</div>
      <div class="spine-pct">${pct(p)} by deadline</div>
    </div>`;
  }

  el.innerHTML = `<div class="spine-axis"></div>${nodes}
    <div style="display:flex;justify-content:space-between;font-size:0.7rem;color:var(--muted);margin-top:4.5rem">
      <span>2026</span><span>2028</span><span>2030</span><span>2032</span>
    </div>`;
}

function renderPaths(cal, path) {
  const buckets = cal?.path_buckets || path?.path_buckets || {};
  let html = "<h2>Path buckets</h2><p class='section-hint'>Named story paths — alignment chain, paralysis, pause stall, etc.</p>";
  for (const [k, p] of Object.entries(buckets).sort((a, b) => b[1] - a[1])) {
    html += bar(k.replace(/_/g, " "), p);
  }
  const sp = path?.spine_paths || {};
  if (Object.keys(sp).length) {
    html += "<h2 style='margin-top:1rem'>Spine prefixes reached</h2>";
    for (const [k, p] of Object.entries(sp).sort((a, b) => b[1] - a[1]).slice(0, 8)) {
      html += bar(k || "none", p, "spine");
    }
  }
  document.getElementById("paths").innerHTML = html;
}

function renderTerminalFlow(path) {
  const raw = path?.terminal_by_spine || {};
  const el = document.getElementById("terminal-flow");
  let html = "<h2>Outcome × spine course</h2><p class='section-hint'>Which terminals follow which capability ladder depth.</p>";
  const entries = Object.entries(raw).sort((a, b) => b[1] - a[1]).slice(0, 12);
  if (!entries.length) {
    el.innerHTML = html + "<p class='muted'>Load path_frequency.json for terminal×spine flows.</p>";
    return;
  }
  for (const [key, p] of entries) {
    const [spine, term] = key.split("|");
    html += `<div class="flow-row">
      <span class="flow-spine" title="${spine}">${spine}</span>
      <span class="flow-arrow">→</span>
      <span class="flow-term" title="${term}">${term}</span>
      <span class="flow-pct">${pct(p)}</span>
    </div>`;
  }
  el.innerHTML = html;
}

function renderTerminals(cal) {
  const terms = cal?.terminals || {};
  let html = "<h2>Terminal distribution</h2>";
  for (const [k, p] of Object.entries(terms).sort((a, b) => b[1] - a[1]).slice(0, 14)) {
    html += bar(k.replace(/_/g, " "), p);
  }
  document.getElementById("terminals").innerHTML = html;
}

function renderSampleRuns(samples) {
  const el = document.getElementById("sample-runs");
  const runs = samples?.runs || [];
  if (!runs.length) {
    el.innerHTML = "<p class='muted'>No sample runs — run <code>python scripts/export_sample_runs.py</code></p>";
    return;
  }
  el.innerHTML = runs.map((run) => {
    const course = (run.timeline || []).map((step) => {
      const when = step.date ? `<span class="when">${step.date.slice(0, 7)}</span>` : "";
      const kind = step.kind === "spine" ? "spine" : "event";
      const name = step.id.replace(/^ev_/, "").replace(/^sp_/, "C");
      return `<li class="${kind}">${when}${name}</li>`;
    }).join("");
    return `<article class="run-card">
      <div class="run-header">
        <span class="run-region ${run.region}">${run.region}</span>
        <span class="run-terminal">${run.terminal} · ${run.terminal_date?.slice(0, 7) || ""}</span>
      </div>
      <ul class="run-course">${course}</ul>
    </article>`;
  }).join("");
}

function renderDashboard({ calibration, pathFrequency, sampleRuns }) {
  document.getElementById("app").hidden = false;
  const regions = calibration?.regions || {};
  if (Object.keys(regions).length) renderRegions(regions);
  renderMeta(calibration, pathFrequency);
  renderSpineCourse(calibration);
  renderPaths(calibration, pathFrequency);
  renderTerminalFlow(pathFrequency);
  renderTerminals(calibration);
  renderSampleRuns(sampleRuns);
}

async function loadJson(url) {
  const res = await fetch(url);
  if (!res.ok) throw new Error(url);
  return res.json();
}

async function loadBundledDemo() {
  const [calibration, pathFrequency, sampleRuns] = await Promise.all([
    loadJson("data/calibration_summary.json"),
    loadJson("data/path_frequency.json"),
    loadJson("data/sample_runs.json").catch(() => ({ runs: [] })),
  ]);
  renderDashboard({ calibration, pathFrequency, sampleRuns });
}

document.getElementById("file").addEventListener("change", async (e) => {
  const file = e.target.files?.[0];
  if (!file) return;
  const data = JSON.parse(await file.text());
  if (data.regions) {
    renderDashboard({ calibration: data, pathFrequency: {}, sampleRuns: { runs: [] } });
  } else if (data.spine_paths) {
    renderDashboard({ calibration: {}, pathFrequency: data, sampleRuns: { runs: [] } });
  } else if (data.runs?.[0]?.timeline) {
    renderDashboard({ calibration: {}, pathFrequency: {}, sampleRuns: data });
  }
});

loadBundledDemo().catch((err) => {
  console.warn("Demo data missing:", err);
  document.getElementById("app").hidden = false;
  document.getElementById("outcomes").innerHTML =
    "<h2>Outcome regions</h2><p class='muted'>Generate data: <code>python scripts/calibration_check.py</code> then copy JSON to <code>web/data/</code></p>";
});
