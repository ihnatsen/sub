const express = require('express');
const app = express();
const port = 5008;

// Serwowanie plików statycznych z katalogu public
app.use(express.static('public'));

// Endpoint do obsługi żądań AJAX
app.get('/data', (req, res) => {
  res.json({ message: 'Hello, AJAX!' });
});

app.listen(port, () => {
  console.log(`Serwer uruchomiony na http://localhost:${port}`);
});
