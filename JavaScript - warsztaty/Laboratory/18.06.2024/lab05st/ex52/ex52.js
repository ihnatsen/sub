const express = require('express');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');

const app = express();
app.use(express.json());

const PORT = 5002;
const SECRET_KEY = 'your-secret-key';

const users = [];

app.post('/register', async (req, res) => {
  const { username, password } = req.body;

  const hashedPassword = await bcrypt.hash(password, 10);

  const user = { id: Date.now(), username, password: hashedPassword };
  users.push(user);

  res.status(201).json({ message: 'Użytkownik zarejestrowany!' });
});

app.post('/login', async (req, res) => {
  const { username, password } = req.body;

  const user = users.find(user => user.username === username);
  if (!user) {
    return res.status(400).json({ message: 'Niepoprawna nazwa użytkownika lub hasło' });
  }

  const isPasswordValid = await bcrypt.compare(password, user.password);
  if (!isPasswordValid) {
    return res.status(400).json({ message: 'Niepoprawna nazwa użytkownika lub hasło' });
  }

  const token = jwt.sign({ id: user.id, username: user.username }, SECRET_KEY, { expiresIn: '1h' });

  res.json({ token });
});

const verifyToken = (req, res, next) => {
  const token = req.headers['authorization'];
  if (!token) {
    return res.status(403).json({ message: 'Brak tokenu' });
  }

  jwt.verify(token, SECRET_KEY, (err, decoded) => {
    if (err) {
      return res.status(500).json({ message: 'Nieudane uwierzytelnianie tokenu' });
    }

    req.user = decoded;
    next();
  });
};

app.get('/protected', verifyToken, (req, res) => {
  res.json({ message: 'To jest zabezpieczona trasa', user: req.user });
});

app.listen(PORT, () => {
  console.log(`Serwer działa na porcie ${PORT}`);
});
