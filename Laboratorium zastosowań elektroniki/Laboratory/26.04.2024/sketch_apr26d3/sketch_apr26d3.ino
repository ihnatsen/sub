int pin13 = 13;
int pin8 =  8;

void setup() {
  // put your setup code here, to run once:
  pinMode(pin13, OUTPUT);
  pinMode(pin8, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(pin13, HIGH);
  Serial.println("Dioda zapaliona");
  delay(500);
  digitalWrite(pin13, LOW);
  Serial.println("Dioda zagaszona");
  delay(500);

  digitalWrite(pin8, HIGH);
  delay(500);
  digitalWrite(pin8, LOW);
  delay(500);
}
