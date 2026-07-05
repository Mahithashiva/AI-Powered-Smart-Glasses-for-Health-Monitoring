#include <Wire.h>
#include <U8g2lib.h>
#include <Adafruit_BME280.h>
#include "MAX30105.h"
#include "heartRate.h"

// ---------------- OLED ----------------
U8G2_SH1106_128X64_NONAME_F_HW_I2C display(U8G2_R0, U8X8_PIN_NONE);

// ---------------- Sensors ----------------
Adafruit_BME280 bme;
MAX30105 maxSensor;

// ---------------- Pins ----------------
#define TOUCH_PIN 5
#define IR_PIN 6

// ---------------- Variables ----------------
bool bmeOK = false;

int mode = 0;
unsigned long lastTouch = 0;

long lastBeat = 0;
float bpmAvg = 0;

float temperature = 0;
float pressure = 0;
float stress = 0;
float spo2 = 98;

// ---------------- Setup ----------------
void setup()
{
  Serial.begin(115200);

  pinMode(TOUCH_PIN, INPUT);
  pinMode(IR_PIN, INPUT);

  Wire.begin();

  // OLED
  display.begin();
  display.setFont(u8g2_font_6x12_tf);

  // BME280
  if (bme.begin(0x76))
  {
    bmeOK = true;
    Serial.println("BME280 Connected");
  }
  else
  {
    Serial.println("BME280 Not Found");
  }

  // MAX30102
  if (!maxSensor.begin(Wire, I2C_SPEED_FAST))
  {
    Serial.println("MAX30102 Not Found");
  }
  else
  {
    maxSensor.setup();
    maxSensor.setPulseAmplitudeRed(0x0A);
    maxSensor.setPulseAmplitudeGreen(0);
  }

  display.clearBuffer();
  display.drawStr(15,30,"SMART GLASSES");
  display.drawStr(25,45,"Initializing...");
  display.sendBuffer();

  delay(2000);
}

// ---------------- Loop ----------------
void loop()
{
  readTouch();

  if(mode==0)
      showEnvironment();

  else if(mode==1)
      showHealth();

  else
      showStress();
}
