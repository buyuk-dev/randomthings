enum Direction {
  CLOCKWISE,
  COUNTERCLOCKWISE,
  STOP,
  INVALID
}
DIRECTIONS[2][2] = {
  {STOP, CLOCKWISE},
  {COUNTERCLOCKWISE, INVALID}
};

struct EngineCtrl {
  int speed, dirA, dirB;

  void turn() {
    digitalWrite(dirA, !digitalRead(dirA));
    digitalWrite(dirB, !digitalRead(dirB));
  }

  void setSpeed(int value) {
    analogWrite(speed, value);
  }

  Direction getDirection() {
    int da = digitalRead(dirA) == HIGH ? 1 : 0;
    int db = digitalRead(dirB) == HIGH ? 1 : 0;
    return DIRECTIONS[da][db];
  }

  void setup() {
    pinMode(speed, OUTPUT);
    pinMode(dirA, OUTPUT);
    pinMode(dirB, OUTPUT);
  }
};

EngineCtrl leftEngine = {5, 7, 8};
EngineCtrl rightEngine = {6, 3, 2};

void setup() {
  leftEngine.setup();
  rightEngine.setup();
}

void loop() {
  delay(1000);
  leftEngine.turn();
  rightEngine.turn();
}
