from __init__ import *
def simultaneous_hue_shift(wait, speed, divisor):
    import math
    pixels.clear()
    for i in range(int(math.floor(256/speed))):
        # color = Adafruit_WS2801.RGB_to_color(0, int(math.floor(255/divisor)), int(math.floor(math.floor(i*speed)/divisor)))
        color = RGB_to_color(0,255,i*speed,divisor)
        for j in range(pixels.count()):
            pixels.set_pixel(j, color)
        pixels.show()
        if wait > 0:
            time.sleep(wait)
    for i in range(int(math.floor(256/speed))):
        # color = Adafruit_WS2801.RGB_to_color(0, int(math.floor((255-math.floor(i*speed))/divisor)), int(math.floor(255/divisor)))
        color = RGB_to_color(0,255-(i*speed),255,divisor)
        for j in range(pixels.count()):
            pixels.set_pixel(j,color)
        pixels.show()
        if wait > 0:
            time.sleep(wait)
    for i in range(int(math.floor(256/speed))):
        # color = Adafruit_WS2801.RGB_to_color(int(math.floor((math.floor(i*speed))/divisor)), 0, int(math.floor(255/divisor)))
        color = RGB_to_color(i*speed,0,255,divisor)
        for j in range(pixels.count()):
            pixels.set_pixel(j,color)
        pixels.show()
        if wait > 0:
            time.sleep(wait)
    for i in range(int(math.floor(256/speed))):
        # color = Adafruit_WS2801.RGB_to_color(int(math.floor(255/divisor)), 0, int(math.floor((255-math.floor(i*speed))/divisor)))
        color = RGB_to_color(255,0,255-(i*speed),divisor)
        for j in range(pixels.count()):
            pixels.set_pixel(j,color)
        pixels.show()
        if wait > 0:
            time.sleep(wait)
