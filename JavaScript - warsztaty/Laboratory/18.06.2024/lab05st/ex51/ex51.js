const express = require('express');
const path = require('path');
const app = express();

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Ustawienie katalogu publicznego na statyczne pliki
app.use(express.static(path.join(__dirname, 'public')));

// Przykładowe dane
const users = [
  { name: 'John Doe', email: 'john@example.com' },
  { name: 'Jane Smith', email: 'jane@example.com' },
  { name: 'Bob Johnson', email: 'bob@example.com' }
];


app.get('/', (req, res) => {
  res.render('pages/index', { title: 'Home', users });
});

app.get('/about', (req, res) => {
  res.render('pages/about', { title: 'About Us' });
});

// Uruchomienie serwera
const PORT = process.env.PORT || 5001;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
