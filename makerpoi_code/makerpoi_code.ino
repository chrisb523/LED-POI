#include <Adafruit_NeoPixel.h>

#define PIN 1
#define NUM_LEDS 32

Adafruit_NeoPixel strip = Adafruit_NeoPixel(32, PIN, NEO_BRG + NEO_KHZ800);

#include "graphicz.h"

void setup() {
  strip.begin();
  strip.setBrightness(12);
}

void loop() {
  int numColors= sizeof(values)/3; //Gets the number of lines in the array
  int current_pixel = 0; //Stores the current pixel

  
  for(int i=0; i<numColors; i++) {
    strip.setPixelColor(current_pixel, values[i][0], values[i][1], values[i][2]); //Sets the current pixel to the three colors on the given line of the array
    strip.show(); 
    
    current_pixel++; 
    
    if (current_pixel == 32)
      current_pixel = 0;
  }
}
  
