require('dotenv').config();
const express = require('express');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');
const bodyParser = require('body-parser');
const path = require('path');

const app = express();
app.use(bodyParser.json());
app.use(express.static(path.join(__dirname, 'public')));

const users = []; // Tożsamości użytkowników przechowujemy w pamięci dla uproszczenia

// Rejestracja użytkownika
app.post('/register', async (req, res) => {
  const { username, password } = req.body;

  const hashedPassword = await bcrypt.hash(password, 10);

  users.push({ username, password: hashedPassword });
  res.status(201).send('User registered');
});

// Logowanie użytkownika
app.post('/login', async (req, res) => {
  const { username, password } = req.body;
  const user = users.find(u => u.username === username);

  if (!user) {
    return res.status(401).send('Invalid credentials');
  }

  const isPasswordValid = await bcrypt.compare(password, user.password);

  if (!isPasswordValid) {
    return res.status(401).send('Invalid credentials');
  }

  const token = jwt.sign({ username: user.username }, process.env.JWT_SECRET, { expiresIn: '1h' });
  res.json({ token });
});

// Middleware do weryfikacji tokena
const authenticateJWT = (req, res, next) => {
  const authHeader = req.headers.authorization;

  if (authHeader) {
    const token = authHeader.split(' ')[1];

    jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
      if (err) {
        return res.sendStatus(403);
      }

      req.user = user;
      next();
    });
  } else {
    res.sendStatus(401);
  }
};

// Chroniony zasób
app.get('/protected', authenticateJWT, (req, res) => {
  res.send('This is a protected resource');
});

// Wylogowanie (opcjonalne)
app.post('/logout', (req, res) => {
  // JWT nie wymaga serwerowego wylogowania, wystarczy usunąć token po stronie klienta
  res.send('Logged out');
});

const PORT = process.env.PORT || 5004;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
