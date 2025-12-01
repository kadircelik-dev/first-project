// runner_js.js
// Kullanım: node runner_js.js code.js
const fs = require('fs');

const file = process.argv[2];
if (!file) {
  console.error("No file provided");
  process.exit(1);
}

const code = fs.readFileSync(file, 'utf-8');
try {
  eval(code);
} catch (err) {
  console.error(err.toString());
}
