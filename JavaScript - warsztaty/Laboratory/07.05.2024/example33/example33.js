const express = require('express');
const cors = require('cors');
const app = express();
const port = 8833;

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

    // Tutaj możesz wykonać operacje na danych, np. zapis do bazy danych

    // Odsyłamy odpowiedź do klienta
    res.send('Car rental data received successfully!');
});


// Nasłuchujemy na porcie 8833
app.listen(port, () => {
  console.log('Aplikacja działa na porcie ' + port);
});