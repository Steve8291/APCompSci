// PHOTOCELL (PHOTO RESISTOR)

const int sensorPin = 0;
const int ledPin = 9;

// global variables for light level
int lightLevel;
int high = 0;
int low = 1023;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);

}

void loop() {
  lightLevel = analogRead(sensorPin);  // 0 Volts = 0, 5 Volts = 1023

  //manualTune();  // manually change the range from light to dark
  autoTune();

  analogWrite(ledPin, lightLevel);

}

void manualTune()
{
  // analogRead gets values from 0 - 1023
  // analogWrite can write values from 0 - 255
  lightLevel = map(lightLevel, 0, 1023, 0, 255);
  // constrain value from 0-255 in case we get something out of range
  lightLevel = constrain(lightLevel, 0, 255);
}


void autoTune()
{
  if (lightLevel < low)
  {
    low = lightLevel;
    Serial.print("LOW: ");
    Serial.println(low);
  }

  if (lightLevel > high)
  {
    high = lightLevel;
    Serial.print("HIGH: ");
    Serial.println(high);
  }

  lightLevel = map(lightLevel, low + 30, high - 30, 0, 255);
  lightLevel = constrain(lightLevel, 0, 255);


}



