
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  delay(1000);
}

void loop() {
  // put your main code here, to run repeatedly:
  int Potencjometr = analogRead(A5);

  Serial.print("Odczyt: ");
  Serial.print(Potencjometr, DEC);
  Serial.print("[DEC]\t");
  Serial.print(Potencjometr, HEX);
  Serial.print("[HEX]\t");
  Serial.print(Potencjometr, OCT);
  Serial.print("[OCT]\t");
  Serial.print(Potencjometr, BIN);
  Serial.print("[BIN]\n");
  
  float delta = 5.0 / 1024.0;
  Serial.print("Delta - ");
  Serial.print(delta, 4);

  float Volt = float (Potencjometr) * delta;
  Serial.print("     Volt - ");
  Serial.print(Volt, 4);
  delay(5000);
}
