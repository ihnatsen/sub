   //Test czujnika PIR HC-SR501
        
    int PIR = 8;   //pin 8 połączony z sygnałem czujnika PIR
     
    void setup(){
      Serial.begin(9600);        //inicjalizacja monitora szeregowego
      pinMode(PIR, INPUT);       //ustawienie pinu PIR jako wejście
      
      Serial.println("Start testu czujnika PIR HC-SR501"); 
    }
     
    void loop(){
      int ruch = digitalRead(PIR);          //odczytanie wartości z czujnika
      if(ruch == HIGH)                      //sprawdzenie stanu odczytu pinu PIR
      {                                     //stan wysoki oznacza wykrycie ruchu
        Serial.println("Wykryty ruch w pomieszczeniu");
      }
      else
      {
        Serial.println("Brak ruchu w pomieszczeniu"); //stan niski oznacza brak ruchu 
      }
      delay(200);                //opóźnienie między kolejnymi odczytami
    }
