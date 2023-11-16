// Demonstrate using a Switch Case Statement to simplify if statements

// Arduino Serial Communication using Python tkinter GUI
// Turns on and off ledPin 13 and fanPin 12
// Python GUI must be running before you attempt to open the Arduino IDE serial montior

const int ledPin = 13;  // Pin LED is attached to
const int fanPin = 12;  // Pin fan is attached to
int incomingByte;       // Variable to store serial data


void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  // initialize pins as output:
  pinMode(ledPin, OUTPUT);
  pinMode(fanPin, OUTPUT);
}

void loop() {
  // See if there is incoming serial data:
  if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();
    Serial.println(incomingByte);

    // Check value of `incomingByte` against each case:
    switch (incomingByte) {
      case 'H':
        digitalWrite(ledPin, HIGH);
        Serial.println("Getting H");
        break;
      case 'L':
        digitalWrite(ledPin, LOW);
        Serial.println("Getting L");
        break;
      case 'R':
        digitalWrite(fanPin, HIGH);
        Serial.println("Getting R");
        break;
      case 'S':
        digitalWrite(fanPin, LOW);
        Serial.println("Getting S");
        break;
    }
  }
}
