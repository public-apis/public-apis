#!/usr/bin/env node
const fs = require('fs');
const path = require('path');

const README = path.join(__dirname, '..', 'README.md');
const text = fs.readFileSync(README, 'utf8');

// Split into sections by ### headings
const sectionBlocks = text.split(/^###\s+/m).slice(1); // skip first (before any ###)

let totalApis = 0;
const bySection = {};
const allApis = [];
let malformedRows = 0;
const dupCheck = {};

for (const block of sectionBlocks) {
  const lines = block.split('\n');
  const section = lines[0].trim();
  const body = lines.slice(1).join('\n');
  const rows = body.match(/^\|.+\|$/gm) || [];

  bySection[section] = { total: 0, httpsYes: 0, httpsNo: 0, corsYes: 0, corsNo: 0, corsUnknown: 0, noAuth: 0 };

  for (let i = 1; i < rows.length; i++) {
    const cols = rows[i].split('|').map(c => c.trim()).filter((_, j) => j > 0 && j < 7);
    if (cols.length < 4) { malformedRows++; continue; }
    if (cols[0] === '---') { continue; } // skip table separator rows

    const nameLink = cols[0];
    const desc = cols[1];
    const authRaw = cols[2].replace(/`/g, '').trim();
    const httpsRaw = (cols[3] || '').toLowerCase();
    const corsRaw = (cols[4] || '').toLowerCase();

    const urlMatch = nameLink.match(/\[([^\]]+)\]\(([^)]+)\)/);
    if (!urlMatch) { malformedRows++; continue; }

    totalApis++;
    bySection[section].total++;
    bySection[section].httpsYes += (httpsRaw === 'yes') ? 1 : 0;
    bySection[section].httpsNo += (httpsRaw === 'no') ? 1 : 0;
    bySection[section].corsYes += (corsRaw === 'yes') ? 1 : 0;
    bySection[section].corsNo += (corsRaw === 'no') ? 1 : 0;
    bySection[section].corsUnknown += (['unknown', 'unkown'].includes(corsRaw) || !corsRaw) ? 1 : 0;
    bySection[section].noAuth += (authRaw === 'No') ? 1 : 0;

    const url = urlMatch[2];
    if (!dupCheck[url]) dupCheck[url] = [];
    dupCheck[url].push({ name: urlMatch[1], section });

    allApis.push({ name: urlMatch[1], url, section, auth: authRaw, https: httpsRaw, cors: corsRaw });
  }
}

const dupUrls = Object.entries(dupCheck).filter(([_, v]) => v.length > 1);
const totalHttpsYes = Object.values(bySection).reduce((s, v) => s + v.httpsYes, 0);
const totalCorsYes = Object.values(bySection).reduce((s, v) => s + v.corsYes, 0);
const totalNoAuth = Object.values(bySection).reduce((s, v) => s + v.noAuth, 0);
const httpsCoverage = totalHttpsYes / totalApis;
const corsYesRate = totalCorsYes / totalApis;
const noAuthRate = totalNoAuth / totalApis;
const healthScore = Math.round((httpsCoverage * 0.4 + corsYesRate * 0.3 + noAuthRate * 0.3) * 100);

console.log('=== public-apis Health Check ===\n');
console.log(`Total APIs: ${totalApis}`);
console.log(`Total sections: ${Object.keys(bySection).length}`);
console.log(`Malformed rows: ${malformedRows}`);
console.log(`Duplicate URLs: ${dupUrls.length}`);

console.log('\n--- Top 10 Sections by Size ---');
Object.entries(bySection).sort((a, b) => b[1].total - a[1].total).slice(0, 10).forEach(([sec, d]) => {
  const httpsPct = ((d.httpsYes / d.total) * 100).toFixed(0);
  const corsPct = ((d.corsYes / d.total) * 100).toFixed(0);
  console.log(`  ${sec}: ${d.total} APIs | HTTPS ${httpsPct}% | CORS ${corsPct}%`);
});

console.log('\n--- Auth Distribution ---');
const authCounts = {};
for (const api of allApis) {
  authCounts[api.auth] = (authCounts[api.auth] || 0) + 1;
}
for (const [auth, count] of Object.entries(authCounts).sort((a, b) => b[1] - a[1])) {
  console.log(`  ${auth}: ${count} (${(count / totalApis * 100).toFixed(1)}%)`);
}

console.log(`\n=== Health Score: ${healthScore}/100 ===`);
console.log(`  HTTPS coverage:  ${(httpsCoverage * 100).toFixed(1)}%`);
console.log(`  CORS Yes rate:   ${(corsYesRate * 100).toFixed(1)}%`);
console.log(`  No-Auth rate:   ${(noAuthRate * 100).toFixed(1)}%`);
console.log(`  Format issues:   ${malformedRows}`);
console.log(`  Duplicate URLs:  ${dupUrls.length}`);

if (dupUrls.length > 0) {
  console.log('\n--- Duplicate URLs (first 5) ---');
  for (const [url, entries] of dupUrls.slice(0, 5)) {
    console.log(`  ${url} (${entries.length}x): ${entries.map(e => e.name).join(', ')}`);
  }
}

const report = {
  generated: new Date().toISOString(),
  totalApis,
  sections: Object.keys(bySection).length,
  healthScore,
  httpsCoverage: +(httpsCoverage * 100).toFixed(1),
  corsYesRate: +(corsYesRate * 100).toFixed(1),
  noAuthRate: +(noAuthRate * 100).toFixed(1),
  formatIssues: malformedRows,
  duplicateUrls: dupUrls.length,
  bySection,
  authDistribution: authCounts,
};
fs.writeFileSync(path.join(__dirname, '..', 'health_report.json'), JSON.stringify(report, null, 2));
console.log('\nReport saved: health_report.json');
