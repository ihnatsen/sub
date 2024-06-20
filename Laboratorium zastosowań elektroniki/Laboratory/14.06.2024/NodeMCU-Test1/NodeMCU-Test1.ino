//NodeMCUv3 - Test 1 - Migajaca dioda
int ledPin = 12; //D6 - podłączona dioda (+)

// funkcja setap uruchamia się raz przy uruchomieniu programu
void setup() {
 pinMode(ledPin, OUTPUT); // pin D6 ustawiamy jako wyjście
}

// funkcja loop uruchamiana jest w nieskończonej pętli
void loop() {
  digitalWrite(ledPin, HIGH);   // włączmy diodę, podajemy stan wysoki
  delay(500);                  // czekamy 0,5 sek.
  digitalWrite(ledPin, LOW);    // wyłączamy diodę, podajemy stan niski
  delay(500);                  // czekamy 0,5 sek.
}
