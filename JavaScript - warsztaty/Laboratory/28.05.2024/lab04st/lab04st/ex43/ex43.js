const express = require('express');
const path = require('path');

const app = express();
const port = 4003;

// Ustawienie katalogu publicznego na statyczne pliki
app.use(express.static(path.join(__dirname, 'public')));

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.listen(port, () => {
  console.log(`Serwer działa na porcie ${port}`);
});