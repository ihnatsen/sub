#define LM35 A0

void setup(){
  
  Serial.begin(9600);
}

void loop(){

  int odczyt_ADC = (analogRead(LM35));

  Serial.print("Aktualna ADC =  ");
  Serial.println(odczyt_ADC);

  Serial.print("Wydrukowanie temperaturę");
  float delta = 5.0/1024.0;
  float Volt = float(odczyt_ADC)*delta;
  float temp = Volt/0.01;
  Serial.println(temp);

  delay(1000);
}