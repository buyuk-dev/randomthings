#include <LiquidCrystal.h>

const int BRIGHTNESS_CTRL = 10;

LiquidCrystal display(2,3,4,5,6,7);

void setBrightness(int value) {
  analogWrite(BRIGHTNESS_CTRL, value);
}

void setup() {
  pinMode(BRIGHTNESS_CTRL, OUTPUT);
  setBrightness(255);
  display.begin(16, 2);
}

float readVoltage(int inputId) {
  return analogRead(inputId) * 5.0 / 1023.0;
}

void loop() {
  float voltage = readVoltage(A5);

  display.clear();
  display.setCursor(5, 1);
  display.print(voltage);
  display.print('V');

  // display.scrollDisplayLeft()
  // display.scrollDisplayRight()

  delay(100);
}
