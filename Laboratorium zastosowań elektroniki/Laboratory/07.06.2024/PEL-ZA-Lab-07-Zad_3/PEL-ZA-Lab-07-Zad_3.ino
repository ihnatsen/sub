 //Test serwo

#include <Servo.h> //Biblioteka obsługi serwo
 
Servo serw;  //utworzenie obiektu serw 
int pozycja = 0; //Aktualna pozycja serwa 0-180
int zmiana = 12; //Co ile ma się zmieniać pozycja serwa?
 
void setup() 
{ 
  serw.attach(9);  //Serwomechanizm podłączony do pinu 9
} 

void loop() 
{  
  if (pozycja < 180) { //Jeśli pozycja mieści się w zakresie
    serw.write(pozycja); //Wykonaj ruch
  } else { //Jeśli nie, to powrót na początek
    pozycja = 0;
  }    
  
  pozycja = pozycja + zmiana; //Zwiększenie aktualnej pozycji serwa
  delay(50); //Opóźnienie dla lepszego efektu                        
}