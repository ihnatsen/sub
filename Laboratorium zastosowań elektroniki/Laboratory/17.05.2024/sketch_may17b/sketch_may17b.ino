int SensorPin = 0;
int Pomiar;

void setup(){
  Serial.begin(19200);
}

void loop(){
  Pomiar = analogRead(SensorPin);
  Serial.println(Pomiar);
  delay(40);
}