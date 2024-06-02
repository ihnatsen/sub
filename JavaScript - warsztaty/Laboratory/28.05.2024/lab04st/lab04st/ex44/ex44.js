const express = require('express');
const path = require('path');

const app = express();
const port = 4004;

// Ustawienie katalogu publicznego na statyczne pliki
app.use(express.static(path.join(__dirname, 'public')));

// Endpoint główny
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index44.html'));
});

// Endpoint do przekierowania
app.get('/old-endpoint', (req, res) => {
  res.redirect('/new-endpoint');
});

app.get('/new-endpoint', (req, res) => {
  res.send('Zostałeś przekierowany do nowego endpointa!');
});

// Uruchomienie serwera
app.listen(port, () => {
  console.log(`Serwer działa na porcie ${port}`);
});