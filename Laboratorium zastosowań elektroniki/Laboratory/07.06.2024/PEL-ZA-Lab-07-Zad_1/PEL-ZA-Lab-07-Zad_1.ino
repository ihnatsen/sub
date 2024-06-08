//PEL-ZA-Lab-07-Zad_1
//Program symulacji działania PWM
//Dioda włączona poprzez rezystor 330 Ohm do pinu 3 (cyfrowego)

int T = 20;             //Okres PWM
int czas_impulsu = 10;  //Czas trwania impulsu "1"

void setup() {
  pinMode(3, OUTPUT); //Konfiguracja pinu 3 jako wyjście
  digitalWrite(3, LOW); //Wyłączenie diody
}
//Przyjmujemy okres PWM - T
void loop() {
  digitalWrite(3, HIGH);  //Włączenie diody
  delay(czas_impulsu);    //czas właczenia diody - czas trwania impulsu
  digitalWrite(3, LOW);   //Wyłączenie diody
  delay(T-czas_impulsu);  //Czas wyłączenia diody
}