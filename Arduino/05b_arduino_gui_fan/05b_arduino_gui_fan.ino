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
    // if it's a capital H, turn on the LED:
    if (incomingByte == 'H') {
      digitalWrite(ledPin, HIGH);
      Serial.println("Getting H");  // print out to serial monitor to check state
    }
    // if it's an L, turn off the LED:
    else if (incomingByte == 'L') {
      digitalWrite(ledPin, LOW);
      Serial.println("Getting L");
    }
    // if it's an R, run the fan:
    else if (incomingByte == 'R') {
      digitalWrite(fanPin, HIGH);
      Serial.println("Getting R");
    }
    // if it's an S, stop the fan:
    else if (incomingByte == 'S') {
      digitalWrite(fanPin, LOW);
      Serial.println("Getting S");
    }
  }
}
