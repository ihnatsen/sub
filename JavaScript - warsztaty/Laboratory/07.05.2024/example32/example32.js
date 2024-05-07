// Importujemy moduł express
const express = require('express');

// Tworzymy nową instancję aplikacji Express
const app = express();

// Definiujemy ścieżkę główną ('/') i obsługujemy żądania GET na tej ścieżce
app.get('/', (req, res) => {
  // Zwracamy odpowiedź "Hello World!"
  res.send('Hello World!');
});

// Nasłuchujemy na porcie 3000
app.listen(8888, () => {
  console.log('Aplikacja działa na porcie 8888!');
});