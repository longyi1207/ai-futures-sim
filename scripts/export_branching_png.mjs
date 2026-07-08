#!/usr/bin/env node
/** Screenshot export-branching.html → PNG (http server on PORT, default 8799). */

import { spawnSync } from "node:child_process";
import { mkdir } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(__dirname, "..");
const outDir = path.join(root, "web", "exports");
const outFile = path.join(outDir, "branching-timeline.png");
const port = process.env.PORT || "8799";
const url = `http://127.0.0.1:${port}/export-branching.html`;

await mkdir(outDir, { recursive: true });

const result = spawnSync(
  "npx",
  [
    "--yes",
    "playwright",
    "screenshot",
    `--wait-for-selector=body[data-ready="1"]`,
    "--viewport-size=1200,720",
    url,
    outFile,
  ],
  { stdio: "inherit", cwd: root },
);

if (result.status !== 0) process.exit(result.status ?? 1);
console.log(`Wrote ${outFile}`);
