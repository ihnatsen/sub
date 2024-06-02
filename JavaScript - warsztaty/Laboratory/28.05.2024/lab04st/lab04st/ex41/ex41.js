const express = require('express');
const cookieParser = require('cookie-parser');

const app = express();
const port = 4002;

// Middleware do parsowania ciasteczek
app.use(cookieParser());

// Route do ustawiania ciasteczek
app.get('/set-cookie', (req, res) => {
  res.cookie('appName', 'ex41', { maxAge: 60000, httpOnly: true });
  res.cookie('lang', 'pl', { maxAge: 60000 });
  res.send('Ciasteczka zostały ustawione!');
});

// Route do odczytywania ciasteczek
app.get('/get-cookie', (req, res) => {
  const cookies = req.cookies;
  res.send(`Odczytane ciasteczka: ${JSON.stringify(cookies)}`);
});

// Route do usuwania ciasteczek
app.get('/clear-cookie', (req, res) => {
  res.clearCookie('appName');
  res.clearCookie('lang');
  res.send('Ciasteczka zostały usunięte!');
});

// Route główna
app.get('/', (req, res) => {

  res.send('Witaj! Przejdź do /set-cookie, /get-cookie lub /clear-cookie, aby ustawić, odczytać lub usunąć ciasteczka.');
});

// Uruchomienie serwera
app.listen(port, () => {
  console.log(`Serwer działa na porcie ${port}`);
});