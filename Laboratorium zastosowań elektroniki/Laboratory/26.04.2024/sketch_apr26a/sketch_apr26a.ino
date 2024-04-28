int pin13 = 13;
int pin8 = 8;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  delay(1000);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(pin13, HIGH);
  delay(200);
  digitalWrite(pin13, LOW);
  delay(200);

  digitalWrite(pin8, HIGH);
  delay(200);
  digitalWrite(pin8, LOW);
  delay(200);

}
