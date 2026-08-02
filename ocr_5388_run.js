const { createWorker } = require('/Users/bitiworm/.workbuddy/binaries/node/workspace/node_modules/tesseract.js');
const fs = require('fs');
const path = require('path');

const dir = '/Users/bitiworm/WorkBuddy/2026-08-02-14-34-15/lehmanbear/rendered_5388_hi';
const outDir = '/Users/bitiworm/WorkBuddy/2026-08-02-14-34-15/lehmanbear/ocr_5388';
fs.mkdirSync(outDir, { recursive: true });

const files = fs.readdirSync(dir).filter(f => f.endsWith('.png')).sort();

(async () => {
  const worker = await createWorker('eng', 1, {
    logger: m => { if (m.status === 'recognizing text') process.stderr.write(`\r${m.userJobId||''} ${Math.round(m.progress*100)}%`); }
  });
  const combined = [];
  for (let i = 0; i < files.length; i++) {
    const f = files[i];
    process.stderr.write(`\n[page ${i+1}/${files.length}] ${f}\n`);
    const { data: { text } } = await worker.recognize(path.join(dir, f));
    fs.writeFileSync(path.join(outDir, `page_${i+1}.txt`), text);
    combined.push(`\n\n=== PAGE ${i+1} ===\n\n` + text);
  }
  fs.writeFileSync(path.join(outDir, 'combined.txt'), combined.join('\n'));
  await worker.terminate();
  process.stderr.write('\nDONE\n');
})().catch(e => { console.error('OCR ERROR', e); process.exit(1); });
