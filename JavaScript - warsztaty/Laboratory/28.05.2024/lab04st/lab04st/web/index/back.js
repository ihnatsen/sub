const express = require('express');
const bodyParser = require('body-parser');
const sqlite3 = require('sqlite3').verbose();
const cors = require('cors');
const bcrypt = require('bcrypt');

const app = express();
const port = 4002;


// Ustawienia body-parser
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(cors());

//const db = new sqlite3.Database(':memory:'); // baza w pamięci
const db = new sqlite3.Database('baza42.sqlite'); // baza na dysku


// Utworzenie tabeli użytkowników
db.serialize(() => {
    db.run('Create table if not exists users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)');

    // Dodanie przykładowego użytkownika z zaszyfrowanym hasłem
    const username = 'admin';
    const password = 'admin123';
    bcrypt.hash(password, 10, (err, hash) => {
        if (err) throw err;
        const stmt = db.prepare('INSERT INTO users (username, password) VALUES (?, ?)');
        stmt.run(username, hash);
        stmt.finalize();
    });
});

// Endpoint do rejestracji nowego użytkownika
app.post('/register', (req, res) => {
    const { username, password } = req.body;
    bcrypt.hash(password, 10, (err, hash) => {
        if (err) {
            res.status(500).send('Błąd serwera');
            return;
        }
        const stmt = db.prepare('INSERT INTO users (username, password) VALUES (?, ?)');
        stmt.run(username, hash, (err) => {
            if (err) {
                res.status(500).send('Błąd serwera');
                return;
            }
            res.send('Rejestracja zakończona pomyślnie');
        });
    });
});

// Endpoint do logowania
app.post('/login', (req, res) => {
    console.log(req.body)
    const { username, password } = req.body;


    db.get('SELECT * FROM users WHERE username = ?', [username], (err, row) => {
        if (err) {
            res.status(500).send('Błąd serwera');
            return;
        }
        if (!row) {
            res.status(401).send('Nieprawidłowa nazwa użytkownika lub hasło');
            return;
        }
        bcrypt.compare(password, row.password, (err, result) => {
            if (result) {
                res.send(`Witaj, ${username}! Zalogowano pomyślnie.`);
            } else {
                res.status(401).send('Nieprawidłowa nazwa użytkownika lub hasło');
            }
        });
    });
});

// Endpoint główny
app.get('/', (req, res) => {
    res.send('Witaj! Użyj endpointu /register do rejestracji i /login do logowania.');
});

// Uruchomienie serwera
app.listen(port, () => {
    console.log(`Serwer działa na porcie ${port}`);

    const express = require('express');
    const cookieParser = require('cookie-parser');


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
});