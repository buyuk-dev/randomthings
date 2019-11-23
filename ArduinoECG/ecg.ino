/**
 * Streaming analog signal from Arduino UNO via serial port. 
 *
 * sizeof(int) == 2B
 * byte order: little endian
 */


/**
 * Configure Arduino.
 */
void setup() {
  Serial.begin(9600);
  pinMode(A0, INPUT);
}


/**
 * Simulating analog input signal.
 */
int sine_wave(double frequency) {
  double t = double(millis()) / 1000.0;
  return 1024.0 * sin(2.0 * 3.1415 * frequency * t);
}


/**
 * Main program loop.
 */
void loop() {
  int sample = analogRead(A0);
  Serial.write(reinterpret_cast<char*>(&sample), 2);
}
