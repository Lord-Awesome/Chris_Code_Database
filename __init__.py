from Adafruit_Python_WS2801 import Adafruit_WS2801
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import time
import random
import math
import itertools
import pickle
import spidev as sp
import numpy as np
spi = sp.SpiDev()
spi.open(0,1)
spi.max_speed_hz = 125000
PIXEL_COUNT = 160
PIXEL_CLOCK = 11
PIXEL_DOUT  = 10
pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, clk=PIXEL_CLOCK, do=PIXEL_DOUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)    
GPIO.setup(16, GPIO.OUT)

	
def RGB_to_color(R,B,G,divisor):
	return(Adafruit_WS2801.RGB_to_color(int(math.floor(R/divisor)),int(math.floor(B/divisor)),int(math.floor(G/divisor))))
