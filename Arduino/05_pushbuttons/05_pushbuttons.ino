// PUSHBUTTONS

const int button1Pin = 2;  // pushbutton 1 pin
const int button2Pin = 3;  // pushbutton 2 pin
const int ledPin =  13;    // LED pin

int ledState = LOW;         // Tracks the current state of the LED.
int lastButtonState = HIGH; // stores pushbutton status (HIGH = 1, LOW = 0)


void setup() {
  // Set up the pushbutton pins to be an input:
  pinMode(button1Pin, INPUT);
  pinMode(button2Pin, INPUT);

  // Set up the LED pin to be an output:
  pinMode(ledPin, OUTPUT);      
}


void loop() {
  lightLed();
//  singleButton();
}


// Light the LED when either button is pressed (LOW)
// Turns off LED when button is relesed (HIGH)
void lightLed() {
  int button1State = digitalRead(button1Pin);
  int button2State = digitalRead(button2Pin);

  if ((button1State == LOW) || (button2State == LOW))
  {
    digitalWrite(ledPin, HIGH);  // turn the LED on, button pressed
  }
  else
  {
    digitalWrite(ledPin, LOW);  // turn the LED off, button released
  }
}

// Use a single button to turn LED on and off.
// Requires that we keep track of the state of the LED and previous button state.
void singleButton(){
  int button1State = digitalRead(button1Pin);  // Pressing button = LOW, releasing = HIGH

  if (button1State != lastButtonState) {   // button1State starts `HIGH`
    lastButtonState = button1State;         // If button pressed `buttonState` is set `LOW`
    if (button1State == HIGH) {             // Releasing button = HIGH and triggers event
      changeState();
    }
  }
}

void changeState() {
  if (ledState == LOW) {
    ledState = HIGH;
  }
  else {
    ledState = LOW;
  }
  digitalWrite(ledPin, ledState);
}
