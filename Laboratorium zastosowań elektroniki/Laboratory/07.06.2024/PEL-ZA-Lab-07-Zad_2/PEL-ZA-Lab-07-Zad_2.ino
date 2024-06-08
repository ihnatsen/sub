//PEL-DB-Lab-08-Zad_2
//Program symulacji działania PWM
//Dioda włączona poprzez rezystor 330 Ohm do pinu 3 (cyfrowego)

#define diodaPIN 3    //Dioda podłączona na 3 pin cyfrowu - PWM

int wypelnienie = 0;  //Zmienne okresla współczynnik wypełnienia
//Funkcja startowa
void setup() {
	pinMode(diodaPIN, OUTPUT);//Konfiguracja pinu jako wyjścia 
  analogWrite(diodaPIN, wypelnienie);
}
//Funkcja wykonywana w petli nieskończonej
void loop() {
  for (int wypelnienie = 0; wypelnienie < 255; wypelnienie ++){
    analogWrite(diodaPIN, wypelnienie); //Ustawienie PWM 
    delay(10); //Opóźnienia dla obserwacji narastania świecenia diody
  }
}