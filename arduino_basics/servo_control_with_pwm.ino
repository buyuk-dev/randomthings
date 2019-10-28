#include <Servo.h>

const int CTRL = A5;
Servo srv;

void setup() {
  Serial.begin(9600);
  srv.attach(3);
  srv.write(0);
}

// controlling servo position via serial port commands.
void loop2() {
  while (Serial.available() == 0) { delay(50); };
  int position = Serial.parseInt();
  if (position >= 0 && position <= 180) {
    srv.write(position);
  }
}

// controlling servo position via potentiometer.
void loop() {
  int reading = analogRead(CTRL);
  int position = map(reading, 550, 1023, 0, 180);
  srv.write(position);
  delay(50);
}
