#include <FastLED.h>
#define LED_PIN         A3
#define NUM_LEDS        10
#define MAX_BRIGHTNESS  100
#define DELAY           200

int input = 1;
CRGB leds[NUM_LEDS];

void setup()
{
  Serial.begin(9600);
  FastLED.addLeds<WS2812B, LED_PIN, GRB>(leds, NUM_LEDS);
  FastLED.setBrightness( MAX_BRIGHTNESS );

}

void loop()   /*----( LOOP: RUNS CONSTANTLY )----*/
{
  if (input == 1)
  {
    notSafe();
  }
  else
  {
    neutral();
  }
}


void notSafe()
{
  FastLED.clear();
  FastLED.setBrightness( MAX_BRIGHTNESS );
  fill_solid( leds, NUM_LEDS, CRGB(255,0,0));

  FastLED.show();
  //delay(500);
}

void safe()
{
  FastLED.clear();
  FastLED.setBrightness( MAX_BRIGHTNESS );
  fill_solid( leds, NUM_LEDS, CRGB(0,255,0));

  FastLED.show();
}

void neutral()
{
  FastLED.clear();
  FastLED.show();

}
