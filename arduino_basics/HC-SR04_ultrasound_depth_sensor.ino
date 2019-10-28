// Arduino GPIO ids
const int TRIGGER = 8;
const int DISTANCE = 9;
const int BUZZER = 10;

// Sensor parameters from spec.
const long MAX_DISTANCE = 400;
const int MIN_TRIGGER_SIG_LENGTH = 10;

// Time in which sound travels by 1cm. From sensor spec.
const long SOUND_SPEED = 58;

long measureDistance() {
  digitalWrite(TRIGGER, HIGH);
  delayMicroseconds(MIN_TRIGGER_SIG_LENGTH);
  digitalWrite(TRIGGER, LOW);
  long measurement = pulseIn(DISTANCE, HIGH) / SOUND_SPEED;
  return measurement > MAX_DISTANCE ? MAX_DISTANCE : measurement;
}

void setup() {
  pinMode(TRIGGER, OUTPUT);
  pinMode(DISTANCE, INPUT);
  pinMode(BUZZER, OUTPUT);
}

// buzzing strenght will be inversly proportional to the measured distance.
void loop() {
  long distance = measureDistance();
  int buzzStrenght = map(MAX_DISTANCE - distance, 0, MAX_DISTANCE, 0, 255);

  analogWrite(BUZZER, buzzStrength);
  delay(30);
}
