/*
 * BLINK LED
 * 
 * Turns an LED on for one second, then off for one second, repeatedly.
 */


void setup() {
  // put your setup code here, to run once:
  // initialize digital pin 13 as an output.
  // Pin 13 has an LED connectd on most Arduino boards.
  pinMode(13, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(13, HIGH);       // turn the LED on (HIGH is the voltage level)
  delay(1000);                  // wait for a second (value in milliseconds)
  digitalWrite(13, LOW);        // turn the LED off by making the voltage LOW
  delay(1000);

}
