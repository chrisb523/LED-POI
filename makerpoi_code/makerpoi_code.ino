#include <Adafruit_NeoPixel.h>

#define PIN 1
#define NUM_LEDS 32

Adafruit_NeoPixel strip = Adafruit_NeoPixel(32, PIN, NEO_BRG + NEO_KHZ800);

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
  int current_pixel = 0;
  for(int i=0; i<2000; i++) {
    strip.setPixelColor(current_pixel, values[i][0], values[i][1], values[i][2]);
    strip.show(); 
    current_pixel++; 
    if (current_pixel == 32)
      current_pixel = 0;
    delay(2);
  }
}
