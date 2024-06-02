const express = require('express');
const cors = require('cors');
const sqlite3 = require('sqlite3').verbose();

const dbFilePath = 'baza.sqlite';
let db = new sqlite3.Database(dbFilePath);

db.serialize(() => {
    db.run(`CREATE TABLE IF NOT EXISTS carRentals (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      vehicleMake TEXT, 
      rentedModel TEXT, 
      registrationNumberReturn TEXT, 
      dateYearOfProduction TEXT, 
      VIN TEXT
  )`);
});
db.close();

function addCarRental(vehicleMake, rentedModel, registrationNumberReturn, dateYearOfProduction, VIN) {
    let db = new sqlite3.Database(dbFilePath);
    db.run(`INSERT INTO carRentals 
          (vehicleMake, rentedModel, registrationNumberReturn, dateYearOfProduction, VIN) 
          VALUES (?, ?, ?, ?, ?)`,
        [vehicleMake, rentedModel, registrationNumberReturn, dateYearOfProduction, VIN],
        (err) => {
            if (err) {
                console.error('Error adding car rental:', err.message);
            } else {
                console.log('Car rental added successfully!');
            }
            db.close();
        }
    );
}

const app = express();
const port = 8835;

app.use(cors());
app.use(express.json());

app.get('/', (req, res) => {
    res.send('Hello World!');
});

app.post('/carRental', (req, res) => {
    const carRental = req.body;
    console.log('Received car rental data:', carRental);

    addCarRental(carRental.vehicleMake, carRental.rentedModel, carRental.registrationNumberReturn, carRental.dateYearOfProduction, carRental.VIN);

    res.send('Car rental data received successfully!');
});

app.get('/getCarsRental', (req, res) => {
    let db = new sqlite3.Database(dbFilePath);

    let sql = `SELECT vehicleMake, rentedModel, registrationNumberReturn, dateYearOfProduction, VIN FROM carRentals`;

    db.all(sql, [], (err, rows) => {
        if (err) {
            res.status(500).json({error: err.message});
            return;
        }
        res.json(rows);
        db.close();
    });
});

app.listen(port, () => {
    console.log('Aplikacja działa na porcie ' + port);
});
