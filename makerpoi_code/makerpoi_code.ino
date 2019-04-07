#include <Adafruit_NeoPixel.h>

#define PIN 1
#define NUM_LEDS 32

Adafruit_NeoPixel strip = Adafruit_NeoPixel(32, PIN, NEO_GBR + NEO_KHZ800);

#include "graphicz.h"

uint8_t  ImageLine = 0;
uint8_t  ImagePixels = 0;
uint8_t  cb; //Current byte
uint8_t  pixelNum = 0; //,

void setup() {
  strip.begin();
  strip.setBrightness(12);
}

void loop() {
  for(int i=0; i<NUM_LEDS; i++) {
    strip.setPixelColor(i, values[i][0], values[i][1], values[i][2]);
    strip.show(); 
    delay(1);
  }
}
