const { createWorker } = require('/Users/bitiworm/.workbuddy/binaries/node/workspace/node_modules/tesseract.js');
const fs = require('fs'), path = require('path');
const dir = 'rendered_fixup';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.png')).sort();
(async () => {
  const w = await createWorker('eng');
  const out = {};
  for (const f of files) {
    const { data: { text } } = await w.recognize(path.join(dir, f));
    out[f] = text.trim();
    console.log(`OCR ${f}: ${text.length} chars`);
  }
  await w.terminate();
  fs.writeFileSync('ocr_fixup.json', JSON.stringify(out, null, 2));
  console.log('wrote ocr_fixup.json');
})();
