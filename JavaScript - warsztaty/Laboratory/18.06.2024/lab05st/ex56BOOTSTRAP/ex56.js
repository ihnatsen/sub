const express = require('express');
const path = require('path');

const app = express();
const port = 5006;

// Serwowanie plików statycznych z katalogu public
app.use(express.static(path.join(__dirname, 'public')));

// Endpoint główny
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'views', 'index.html'));
});

app.listen(port, () => {
  console.log(`Serwer uruchomiony na http://localhost:${port}`);
});
