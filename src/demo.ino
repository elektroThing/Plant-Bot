#include "Freenove_WS2812_Lib_for_ESP32.h"
#include "DFRobot_SHT20.h"

//  PIN ASSIGNMENTS
int led_sig = 3;
int sig_read = 4;
int sig = 7;
int sda = 19;
int scl = 18;
int in1 = 0;
int in2 = 1;
int capstr = 2;
int neo_pin = 10;
int blk = 5;
//  VARIABLES
int col = 0;
int cycle_time = 2000; //ms
int last_switch_ts = 0;
bool pumpOn = false;

//  PERIPHERALS
Freenove_ESP32_WS2812 strip = Freenove_ESP32_WS2812(1, neo_pin, 0, TYPE_GRB);
DFRobot_SHT20 sht20(&Wire, SHT20_I2C_ADDR);

void setup()
{
  Serial.begin(115200); // The baudrate of Serial monitor is set in 9600
  while (!Serial); // Waiting for Serial Monitor
  pinMode(sig_read, INPUT);
  pinMode(blk, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  strip.begin();
  strip.setBrightness(10);

  sht20.initSHT20();
  delay(100);
  Serial.println("Sensor init finish!");
  sht20.checkSHT20();
}

void loop()
{
  //  DEMO: NEOPIXEL
  if (col < 255)
  {
    col += 1;
  }
  else
  {
    col = 0;
  }
  strip.setLedColorData(0, strip.Wheel((0 / 1 + col) & 255));
  strip.show();

  //  DEMO: SOIL MOISTURE SENSOR
  int moisture = 100 - 100.0 * (analogRead(sig_read) - 1800) / (2700 - 1800); //mapping to max and min

  //  DEMO: WATER PUMP (5VDC)
  if (millis() > last_switch_ts + cycle_time && !pumpOn)
  {
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
    pumpOn = true;
    last_switch_ts = millis();
  }
  else if (millis() > last_switch_ts + cycle_time && pumpOn)
  {
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
    pumpOn = false;
    last_switch_ts = millis();
  }
  digitalWrite(blk,pumpOn);
  digitalWrite(led_sig,pumpOn);

    //  DEMO: SHT20
    float humd = sht20.readHumidity(); //Read the measured data of air humidity
    float temp = sht20.readTemperature(); //Read the measured temp data

    //  DEMO: PRINT OUTPUT
    Serial.print(" Temperature:");
    Serial.print(temp, 1);   // Only print one decimal place
    //  Serial.print("C");
    Serial.print(" Humidity:");
    Serial.print(humd, 1);   // Only print one decimal place
    //  Serial.print("%");
    Serial.print(" Moisture:");
    Serial.print(moisture, 1); //mapping to max and min
    Serial.println();

    delay(100);
}
