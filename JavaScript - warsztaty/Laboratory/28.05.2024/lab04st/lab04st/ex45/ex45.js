const express = require('express');
const session = require('express-session');
const bodyParser = require('body-parser');
const bcrypt = require('bcrypt');
const { v4: uuidv4 } = require('uuid');

const app = express();
const PORT = 4005;

app.use(bodyParser.urlencoded({ extended: true }));
app.use(session({
  secret: 'mySecretKey',
  resave: false,
  saveUninitialized: true,
  cookie: { secure: false } // Ustaw na true w produkcji (HTTPS)
}));

app.use((req, res, next) => {
  if (!req.session.id) {
    req.session.id = uuidv4();
  }
  next();
});


// Do modyfikacji na laboratoriach
const users = [
  { id: 1, username: 'admin', passwordHash: bcrypt.hashSync('admin123', 10) }
];

// Middleware do sprawdzania, czy użytkownik jest zalogowany
function isAuthenticated(req, res, next) {
  if (req.session.userId) {
    next();
  } else {
    res.redirect('/login');
  }
}

app.get('/', isAuthenticated, (req, res) => {
  res.send(`Hello, ${req.session.username}! <a href="/logout">Wyloguj się</a><br>Twój identyfikator sesji to: ${req.session.id}`);
});

app.get('/login', (req, res) => {
  res.send(`
    <form action="/login" method="post">
      <div>
        <label>Nazwa użytkownika:</label>
        <input type="text" name="username">
      </div>
      <div>
        <label>Hasło:</label>
        <input type="password" name="password">
      </div>
      <div>
        <button type="submit">Zaloguj się</button>
      </div>
    </form>
  `);
});

app.post('/login', (req, res) => {
  const { username, password } = req.body;
  const user = users.find(u => u.username === username);

  if (user && bcrypt.compareSync(password, user.passwordHash)) {
    req.session.userId = user.id;
    req.session.username = user.username;
    res.redirect('/');
  } else {
    res.send('Nieprawidłowa nazwa użytkownika lub hasło');
  }
});

app.get('/logout', (req, res) => {
  req.session.destroy(err => {
    if (err) {
      return res.redirect('/');
    }
    res.clearCookie('connect.sid');
    res.redirect('/login');
  });
});

app.listen(PORT, () => {
  console.log(`Serwer działa na porcie ${PORT}`);
});