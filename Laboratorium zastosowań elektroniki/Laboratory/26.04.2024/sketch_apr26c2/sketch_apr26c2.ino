void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  delay(1000);
  Serial.print("Hello, world!");
}

void loop() {
  for(int i=0; i<20; ++i){
    Serial.println(i);
    Serial.println(-i);
    
    delay(100);
  }

}
