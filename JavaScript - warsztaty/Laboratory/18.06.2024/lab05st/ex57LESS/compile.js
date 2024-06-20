const less = require('less');
const fs = require('fs');
const path = require('path');

// Ścieżki do plików Less i CSS
const lessFile = path.join(__dirname, 'less', 'styles.less');
const cssFile = path.join(__dirname, 'css', 'styles.css');

// Funkcja do kompilowania Less do CSS
function compileLess() {
  fs.readFile(lessFile, 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }

    less.render(data, (err, output) => {
      if (err) {
        console.error(err);
        return;
      }

      fs.writeFile(cssFile, output.css, (err) => {
        if (err) {
          console.error(err);
          return;
        }
        console.log('Kompilacja Less do CSS zakończona sukcesem.');
      });
    });
  });
}

// Wywołanie funkcji kompilującej
compileLess();
