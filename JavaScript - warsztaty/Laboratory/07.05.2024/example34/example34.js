const express = require('express');
const cors = require('cors');
const sqlite3 = require('sqlite3').verbose();

let db = new sqlite3.Database('baza.sqlite');
db.serialize(() => {
  db.run("CREATE TABLE IF NOT EXISTS carRentals (id INTEGER PRIMARY KEY AUTOINCREMENT, vehicleRegistrationNumber TEXT, rentedDate TEXT, dateOfReturn TEXT)");
});
db.close();

function addCarRental(vehicleRegistrationNumber, rentedDate, dateOfReturn) {
  db.run("INSERT INTO carRentals (vehicleRegistrationNumber, rentedDate, dateOfReturn) VALUES (?, ?, ?)",
      [vehicleRegistrationNumber, rentedDate, dateOfReturn],
      (err) => {
          if (err) {
              console.error('Error adding car rental:', err.message);
          } else {
              console.log('Car rental added successfully!');
          }
      }
  );
}

const app = express();
const port = 8834;

app.use(cors());
app.use(express.json());

// Definiujemy ścieżkę główną ('/') i obsługujemy żądania GET na tej ścieżce
app.get('/', (req, res) => {
  // Zwracamy odpowiedź "Hello World!"
  res.send('Hello World!');
});

// Obsługa żądania POST na adresie /carRental
app.post('/carRental', (req, res) => {
    // Odbieramy obiekt carRental przesłany z formularza
    const carRental = req.body;
    console.log('Received car rental data:', carRental);

    console.log("carRental:  "+carRental)
    console.log("carRental:  "+carRental.vehicleRegistrationNumber)



    // Tutaj możesz wykonać operacje na danych, np. zapis do bazy danych
    // Tworzymy połączenie z bazą danych SQLite (plik bazy danych)
    db = new sqlite3.Database('baza.sqlite');

    // Tworzymy tabelę w bazie danych (jeśli nie istnieje)
    db.serialize(() => {
      db.run("CREATE TABLE IF NOT EXISTS carRentals (id INTEGER PRIMARY KEY AUTOINCREMENT, vehicleRegistrationNumber TEXT, rentedDate TEXT, dateOfReturn TEXT)");
    });
    addCarRental(carRental.vehicleRegistrationNumber, carRental.rentedDate, carRental.dateOfReturn)
    db.close();


    // Odsyłamy odpowiedź do klienta
    res.send('Car rental data received successfully!');
});


app.listen(port, () => {
  console.log('Aplikacja działa na porcie ' + port);
});

