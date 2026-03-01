// Pin Definitions
#define RAIN_SENSOR_PIN A0
#define TRIG_PIN 9
#define ECHO_PIN 10

void setup() {
  Serial.begin(9600);

  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
}

float readUltrasonicDistance() {
  // Ensure clean trigger pulse
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);

  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  long duration = pulseIn(ECHO_PIN, HIGH);

  // Convert to distance in cm
  float distance = duration * 0.0343 / 2.0;

  return distance;
}

void loop() {
  // Read rain sensor (0–1023)
  int rainValue = analogRead(RAIN_SENSOR_PIN);

  // Read ultrasonic sensor
  float distance = readUltrasonicDistance();

  // Determine rain status (simple threshold logic)
  bool rainStatus;
  if (rainValue < 700) {
    rainStatus = true;
  } else {
    rainStatus = false;
  }

  // Print JSON-style dictionary output
  Serial.print("{ ");
  Serial.print("\"rain_raw\": ");
  Serial.print(rainValue);
  Serial.print(", ");

  Serial.print("\"rain_status\": \"");
  Serial.print(rainStatus);
  Serial.print("\", ");

  Serial.print("\"distance_cm\": ");
  Serial.print(distance);
  Serial.println(" }");

  delay(1000);
}