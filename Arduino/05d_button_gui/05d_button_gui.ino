// Two-way serial communication with Arduino pushbutton and tkinter GUI
// Turns on and off ledPin 13 with a GUI button and physical pushbutton
// Python GUI must be running before you attempt to open the Arduino IDE serial montior

const int ledPin = 13;  // Pin LED is attached to
const int buttonPin = 7;  // Pin button is attached to

// `byte` is an Arduino data type. Unsigned 8 bit int
// It is aliased to the C data type `uint8_t`
// It can hold an unsigned number from 0 - 255
// https://learn.sparkfun.com/tutorials/data-types-in-arduino/all
byte lastButtonState = LOW; // stores pushbutton status (HIGH = 1, LOW = 0)
byte ledState = LOW;        // stores ledState to write to pin
byte incomingByte;          // stores incoming serial data from GUI



void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  // initialize pins as output:
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT);
}

void loop() {
  checkGUI();
  checkBoard();
}


void changeState() {
  if (ledState == LOW) {
    ledState = HIGH;
    Serial.write('H');  // Send serial data to python GUI
  }
  else {
    ledState = LOW;
    Serial.write('L');
  }

  digitalWrite(ledPin, ledState);
}


void checkGUI() {
  // See if there is incoming serial data:
  if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();
    Serial.println(incomingByte);

    // Check value of `incomingByte` against each case:
    switch (incomingByte) {
      case 'H':
        if (ledState != HIGH) {
          changeState();
        }
        break;
      case 'L':
        if (ledState != LOW) {
          changeState();
        }
        break;
    }
  }
}


void checkBoard() {
  byte buttonState = digitalRead(buttonPin);       // Pressing button = HIGH, releasing = LOW
  if (buttonState != lastButtonState) {            // buttonState starts `LOW`
    lastButtonState = buttonState;                 // If button pressed `buttonState` is set `HIGH`
    if (buttonState == LOW) {                      // Releasing button = LOW and triggers event
      changeState();
    }
  }
}

