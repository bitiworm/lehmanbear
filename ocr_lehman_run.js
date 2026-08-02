const { createWorker } = require('/Users/bitiworm/.workbuddy/binaries/node/workspace/node_modules/tesseract.js');
const fs = require('fs'), path = require('path');
const base = '/Users/bitiworm/WorkBuddy/2026-08-02-14-34-15/lehmanbear/rendered_lehman';
const out = '/Users/bitiworm/WorkBuddy/2026-08-02-14-34-15/lehmanbear/ocr_lehman_results.json';
const dirs = ['vol7','vol8'];
const jobs = [];
for (const v of dirs) {
  const d = path.join(base, v);
  for (const f of fs.readdirSync(d)) {
    if (f.endsWith('.png')) {
      const m = f.match(/p(\d+)/);
      if (m) jobs.push({ vol: v, page: parseInt(m[1],10), file: path.join(d, f) });
    }
  }
}
jobs.sort((a,b)=> a.vol.localeCompare(b.vol) || a.page-b.page);
console.error(`total jobs: ${jobs.length}`);
const NWORK = 3;
const results = {};
let ji = 0;
(async () => {
  const workers = await Promise.all(Array.from({length:NWORK}, ()=> createWorker('eng')));
  async function loop(w){
    while (ji < jobs.length) {
      const j = jobs[ji++];
      try {
        const { data:{text} } = await w.recognize(j.file);
        results[j.vol] = results[j.vol] || {};
        results[j.vol][j.page] = text;
        process.stderr.write(`done ${j.vol} p${j.page} (${ji}/${jobs.length})\n`);
      } catch(e){ process.stderr.write(`ERR ${j.vol} p${j.page} ${e}\n`); }
    }
  }
  await Promise.all(workers.map(loop));
  await Promise.all(workers.map(w=>w.terminate()));
  fs.writeFileSync(out, JSON.stringify(results));
  console.error('WROTE ' + out);
})();
