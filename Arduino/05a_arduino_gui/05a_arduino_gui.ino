// Arduino Serial Communication using Python tkinter GUI
// Turns on and off ledPin 13
// Python GUI must be running before you attempt to open the Arduino IDE serial montior

const int ledPin = 13;  // Pin LED is attached to
int incomingByte;       // Variable to store serial data


void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  // initialize LED pin as an output:
  pinMode(ledPin, OUTPUT);
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
    if (incomingByte == 'L') {
      digitalWrite(ledPin, LOW);
      Serial.println("Getting L");
    }
  }
}
