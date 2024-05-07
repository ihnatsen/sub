const express = require('express');
const cors = require('cors');
const sqlite3 = require('sqlite3').verbose();

let db = new sqlite3.Database('baza.sqlite');
db.serialize(() => {
  db.run("CREATE TABLE IF NOT EXISTS carRentals (id INTEGER PRIMARY KEY AUTOINCREMENT, vehicleRegistrationNumber TEXT, rentedDate TEXT, dateOfReturn TEXT, lastName TEXT, secondName TEXT, PESEL TEXT)");
});
db.close();

function addCarRental(vehicleRegistrationNumber, rentedDateDisplay, dateOfReturnDisplay, lastName, secondName, PESEL) {
  db.run("INSERT INTO carRentals (vehicleRegistrationNumber, rentedDate, dateOfReturn,lastName, secondName, PESEL) VALUES (?, ?, ?, ?, ? ,?)",
      [vehicleRegistrationNumber, rentedDateDisplay, dateOfReturnDisplay,lastName,secondName,PESEL],
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
const port = 8835;

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
      db.run("CREATE TABLE IF NOT EXISTS carRentals (id INTEGER PRIMARY KEY AUTOINCREMENT, vehicleRegistrationNumber TEXT, rentedDateDisplay TEXT, dateOfReturnDisplay TEXT, lastName TEXT, secondName TEXT, PESEL TEXT)");
    });
    //        this.PESEL = PESEL;
    //         this.lastName = lastName;
    //         this.secondName = secondName;
    addCarRental(carRental.vehicleRegistrationNumber, carRental.rentedDate, carRental.dateOfReturn, carRental.PESEL, carRental.lastName, carRental.secondName)
    db.close();


    // Odsyłamy odpowiedź do klienta
    res.send('Car rental data received successfully!');
});

// Definiujemy endpoint /getCarsRental, który zwraca dane z tabeli carRental
app.get('/getCarsRental', (req, res) => {
  // Zapytanie SQL do pobrania danych z tabeli carRental
  
  db = new sqlite3.Database('baza.sqlite');

  let sql = `SELECT vehicleRegistrationNumber, rentedDate, dateOfReturn, lastName, secondName, PESEL FROM carRentals`;


  // Wykonujemy zapytanie SQL
  db.all(sql, [], (err, rows) => {
    if (err) {
      throw err;
    }
    // Zwracamy dane w formacie JSON
    res.json(rows);
  });

  db.close();
});


app.listen(port, () => {
  console.log('Aplikacja działa na porcie ' + port);
});

