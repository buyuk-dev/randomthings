void setup() {
  Serial.begin(9600);
  pinMode(A0, INPUT);
}

void loop() {
  int sample = analogRead(A0);
  Serial.write(sample);
}
