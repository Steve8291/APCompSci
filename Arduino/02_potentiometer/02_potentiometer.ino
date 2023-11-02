/*
POTENTIOMETER

  Measure the position of a potentiometer and use it to
  control the blink rate of an LED. Turn the knob to make
  it blink faster or slower!

What's a potentiometer?

  A potentiometer, or "pot" for short, is a control knob.
  It's the same type of control you'd use to change volume, 
  dim a lamp, etc. A potentiometer changes resistance as it
  is turned. By using it as a "voltage divider", the Arduino
  can sense the position of the knob, and use that value to
  control whatever you wish (like the blink rate of an LED,
  as we're doing here).

  Potentiometer:
  
    Potentiometers have three pins. When we're using it as a
    voltage divider, we connect the outside pins to power and
    ground. The middle pin will be the signal (a voltage which
    varies from 0 Volts to 5 Volts depending on the position of
    the knob).

    Connect the middle pin to ANALOG IN pin 0 on the Arduino.
    Connect one of the outside pins to 5V.
    Connect the other outside pin to GND.

    (TIP: if once your program is running, the knob feels
    "backwards", you can swap the 5V and GND pins to reverse
    the direction.)
*/

// Create a variable called "sensorPin" of type "int"
// and initialize it to have the value "0":

int sensorPin = 0;    // The potentiometer is connected to
                      // analog pin 0
                      
int ledPin = 13;      // The LED is connected to digital pin 13

// One more thing. If you declare variables outside of a function,
// as we have here, they are called "global variables" and can be
// seen by all the functions. If you declare variables within a 
// function, they can only be seen within that function. It's good
// practice to "limit the scope" of a variable whenever possible,
// but as we're getting started, global variables are just fine.


void setup() // this function runs once when the sketch starts up
{
  // We'll be using pin 13 to light a LED, so we must configure it
  // as an output.
 
  // Because we already created a variable called ledPin, and
  // set it equal to 13, we can use "ledPin" in place of "13".
  // This makes the sketch easier to follow.
  
  pinMode(ledPin, OUTPUT);
  
  // The above line is the same as "pinMode(13, OUTPUT);"

  // You might be wondering why we're not also configuring
  // sensorPin as an input. The reason is that this is an
  // "analog in" pin. These pins have the special ability to
  // read varying voltages from sensors like the potentiometer.
  // Since they're always used as inputs, there is no need to
  // specifically configure them.
}


void loop() // this function runs repeatedly after setup() finishes
{
  // First we'll declare another integer variable
  // to store the value of the potentiometer:

  int sensorValue;

  // The potentiometer is set up as a voltage divider, so that
  // when you turn it, the voltage on the center pin will vary
  // from 0V to 5V. We've connected the center pin on the
  // potentiometer to the Arduino's analog input 0.

  // The Arduino can read external voltages on the analog input
  // pins using a built-in function called analogRead(). This
  // function takes one input value, the analog pin we're using
  // (sensorPin, which we earlier set to 0). It returns an integer
  // number that ranges from 0 (0 Volts) to 1023 (5 Volts).
  // We're sticking this value into the sensorValue variable:

  sensorValue = analogRead(sensorPin);    

  // Now we'll blink the LED like in the first example, but we'll
  // use the sensorValue variable to change the blink speed
  // (the smaller the number, the faster it will blink).

  // Note that we're using the ledPin variable here as well:

  digitalWrite(ledPin, HIGH);     // Turn the LED on

  delay(sensorValue);             // Pause for sensorValue
                                  // milliseconds
  
  digitalWrite(ledPin, LOW);      // Turn the LED off

  delay(sensorValue);             // Pause for sensorValue
                                  // milliseconds
  
  // Remember that loop() repeats forever, so we'll do all this
  // again and again.
}
