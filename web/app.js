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

function renderCalibration(data) {
  document.getElementById("app").hidden = false;
  document.getElementById("meta").innerHTML = `
    <h2>Run</h2>
    <table>
      <tr><th>Runs</th><td>${data.runs}</td></tr>
      <tr><th>Seed</th><td>${data.seed}</td></tr>
      <tr><th>Early absorb</th><td>${pct(data.early_absorb_rate || 0)}</td></tr>
      <tr><th>Horizon assign</th><td>${pct(data.horizon_absorb_rate || 0)}</td></tr>
      <tr><th>Monotonic spine</th><td>${data.monotonic_spine ? "✓" : "✗"}</td></tr>
    </table>`;

  const regions = data.regions || {};
  let regHtml = "<h2>Outcome regions (emergent)</h2>";
  for (const k of ["doom", "utopia", "friction", "severe"]) {
    regHtml += bar(k, regions[k] || 0, k);
  }
  document.getElementById("regions").innerHTML = regHtml;

  const spine = data.spine_by_deadline || {};
  let spineHtml = "<h2>Spine by deadline</h2>";
  for (const [mid, p] of Object.entries(spine)) {
    const med = (data.spine_median_day || {})[mid] || "—";
    spineHtml += `<div class="bar-row"><div class="bar-label"><span>${mid}</span><span>${pct(p)} · ${med}</span></div></div>`;
  }
  document.getElementById("spine").innerHTML = spineHtml;

  const paths = data.path_buckets || {};
  let pathHtml = "<h2>Path buckets</h2>";
  for (const [k, p] of Object.entries(paths).sort((a, b) => b[1] - a[1])) {
    pathHtml += bar(k, p);
  }
  document.getElementById("paths").innerHTML = pathHtml;

  const terms = data.terminals || {};
  let termHtml = "<h2>Terminals</h2>";
  for (const [k, p] of Object.entries(terms).sort((a, b) => b[1] - a[1]).slice(0, 14)) {
    termHtml += bar(k, p);
  }
  document.getElementById("terminals").innerHTML = termHtml;
}

function renderPathFrequency(data) {
  document.getElementById("app").hidden = false;
  document.getElementById("meta").innerHTML = `<h2>Path frequency</h2><p>${data.runs} runs · seed ${data.seed}</p>`;

  const sp = data.spine_paths || {};
  let spineHtml = "<h2>Spine prefix</h2>";
  for (const [k, p] of Object.entries(sp).sort((a, b) => b[1] - a[1]).slice(0, 10)) {
    spineHtml += bar(k || "none", p);
  }
  document.getElementById("spine").innerHTML = spineHtml;

  const buckets = data.path_buckets || {};
  let pathHtml = "<h2>Path buckets</h2>";
  for (const [k, p] of Object.entries(buckets).sort((a, b) => b[1] - a[1])) {
    pathHtml += bar(k, p);
  }
  document.getElementById("paths").innerHTML = pathHtml;

  document.getElementById("regions").innerHTML = "<h2>Event signatures</h2>" +
    Object.entries(data.event_paths || {}).slice(0, 8).map(([k, p]) => bar(k.slice(0, 40), p)).join("");

  document.getElementById("terminals").innerHTML = "<h2>Terminal × spine</h2>" +
    Object.entries(data.terminal_by_spine || {}).slice(0, 10).map(([k, p]) => bar(k, p)).join("");
}

document.getElementById("file").addEventListener("change", async (e) => {
  const file = e.target.files?.[0];
  if (!file) return;
  const data = JSON.parse(await file.text());
  if (data.spine_by_deadline) renderCalibration(data);
  else renderPathFrequency(data);
});
