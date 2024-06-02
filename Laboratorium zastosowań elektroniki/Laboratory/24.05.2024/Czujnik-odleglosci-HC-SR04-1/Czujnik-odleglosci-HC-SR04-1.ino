// Test czujnika odległosci-1
// Czujnik odległosi HC-SR04

#define trigPin 12
#define echoPin 11


void setup() {
  Serial.begin (9600);
  delay(500);
  Serial.println("Start orogramu testu czujnika odległości HC-SR04");
  //Ustawienie pinów Arduino dla czujnika odległosci
  pinMode(trigPin, OUTPUT); //Pin 12 - do którego podłączymy trig jako wyjście
  pinMode(echoPin, INPUT); //Pin 11 - do którego podłączone echo jako wejście
}

void loop() {
// Wywołanie funkcji zmierzOdległość() i wydruk wartosci na monitorze
  Serial.print(zmierzOdleglosc());
  Serial.println(" cm");
  delay(500);
} 
// Definicja funkcji pomiaru odległości przedmiotu od czujnika w cm
int zmierzOdleglosc() {
  long czas, dystans;

  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
// Zastosowanie standardowej funkcji pulseIn() 
// Funkcja pulseIn() mierzy czas trwania impulsu na pinie cyfrowym
// Czas trwania impulsu określa odległość przedmiotu od czujnika
  czas = pulseIn(echoPin, HIGH);
// Obliczenie odległości przedmiotu od czujnika w cm
// Liczba "58" jest stałą wynikającą z konstrukcji czujnika
  dystans = czas / 58;
// Funkcja zwraca odległość przedmiotu od czujnika w cm
  return dystans;
}