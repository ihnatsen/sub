const fs = require('fs');
const path = require('path');

// Ścieżki do plików Bootstrap
const bootstrapCssPath = path.join(__dirname, '../node_modules/bootstrap/dist/css/bootstrap.min.css');
const bootstrapJsPath = path.join(__dirname, '../node_modules/bootstrap/dist/js/bootstrap.min.js');
const jqueryJsPath = path.join(__dirname, '../node_modules/jquery/dist/jquery.min.js');
const popperJsPath = path.join(__dirname, '../node_modules/popper.js/dist/umd/popper.min.js');

// Ścieżki docelowe
const publicCssDir = path.join(__dirname, '../public/css');
const publicJsDir = path.join(__dirname, '../public/js');

// Upewnienie się, że katalogi docelowe istnieją
if (!fs.existsSync(publicCssDir)) {
  fs.mkdirSync(publicCssDir, { recursive: true });
}
if (!fs.existsSync(publicJsDir)) {
  fs.mkdirSync(publicJsDir, { recursive: true });
}

// Funkcja kopiująca plik
function copyFile(src, dest) {
  fs.copyFileSync(src, dest);
  console.log(`Skopiowano ${src} do ${dest}`);
}

// Kopiowanie plików
copyFile(bootstrapCssPath, path.join(publicCssDir, 'bootstrap.min.css'));
copyFile(bootstrapJsPath, path.join(publicJsDir, 'bootstrap.min.js'));
copyFile(jqueryJsPath, path.join(publicJsDir, 'jquery.min.js'));
copyFile(popperJsPath, path.join(publicJsDir, 'popper.min.js'));
