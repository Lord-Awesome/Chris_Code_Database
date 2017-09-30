from Adafruit_Python_WS2801 import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI
import time
import random
import math
PIXEL_COUNT = 160
PIXEL_CLOCK = 11
PIXEL_DOUT  = 10
pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, clk=PIXEL_CLOCK, do=PIXEL_DOUT)

def RGB_to_color(R,B,G,divisor):
	return(Adafruit_WS2801.RGB_to_color(int(math.floor(R/divisor)),int(math.floor(B/divisor)),int(math.floor(G/divisor))))
	
