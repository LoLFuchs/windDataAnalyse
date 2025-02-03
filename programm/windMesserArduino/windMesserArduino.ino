#define MOTOR_IN A1
#define THRESHOLD_POWER 25
#define LED_GROUND 2
#define LED_PLUS 3

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(LED_GROUND, OUTPUT);
  pinMode(LED_PLUS, OUTPUT);
  digitalWrite(LED_GROUND, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  int voltage = analogRead(MOTOR_IN);
  Serial.println(voltage);
  if (voltage > THRESHOLD_POWER) {
    digitalWrite(LED_PLUS, HIGH);
  }
  else {
    digitalWrite(LED_PLUS, LOW);
  }
}
