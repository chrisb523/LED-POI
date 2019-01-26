#include <Adafruit_NeoPixel.h>
#include "imagez.h"
#define PIN 1

// Parameter 1 = number of pixels in strip
// Parameter 2 = Trinket m0 pin number (Only pin 1 is valid for PMW)
// Parameter 3 = pixel type flags, add together as needed:
//   NEO_KHZ800  800 KHz bitstream (most NeoPixel products w/WS2812 LEDs)
//   NEO_KHZ400  400 KHz (classic 'v1' (not v2) FLORA pixels, WS2811 drivers)
//   NEO_GRB     Pixels are wired for GRB bitstream (most NeoPixel products)
//   NEO_RGB     Pixels are wired for RGB bitstream (v1 FLORA pixels, not v2)
Adafruit_NeoPixel strip = Adafruit_NeoPixel(144, PIN, NEO_GRB + NEO_KHZ800);

// IMPORTANT: To reduce NeoPixel burnout risk, add 1000 uF capacitor across
// pixel power leads, add 300 - 500 Ohm resistor on first pixel's data input
// and minimize distance between Arduino and first pixel. Avoid connecting
// on a live circuit... if you must, connect GND first.

void setup() {
  strip.begin();
  strip.setBrightness(50);
  strip.show(); // initialize all pixels to "off"
}

void imageinit() {
  //File file=new File("graphics.h");
  
  //int rgbArray = file.read().split('\n');
  //int size = len(rgbArray); **/
}

void loop() {
  for i in range(0, size):
    i=i+1;
    //strip.setPixelColor(rgbArray[i]);
}
