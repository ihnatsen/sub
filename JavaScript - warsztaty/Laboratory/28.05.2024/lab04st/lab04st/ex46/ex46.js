const express = require('express');
const path = require('path');
const app = express();
const PORT = 4006;

// Ustawienie EJS jako silnika szablonów
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Obsługa statycznych plików
app.use(express.static(path.join(__dirname, 'public')));

// Strona główna
app.get('/', (req, res) => {
  const data = { title: 'Strona główna', message: 'Witaj na stronie głównej!' };
  res.render('index', data);
});

// Strona o nas
app.get('/about', (req, res) => {
  const data = { title: 'O nas', message: 'To jest strona o nas.' };
  res.render('about', data);
});

app.listen(PORT, () => {
  console.log(`Serwer działa na porcie ${PORT}`);
});