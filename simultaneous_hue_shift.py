from __init__ import *
def simultaneous_hue_shift(wait, speed, divisor):
    import math
    for i in range(math.floor(256/speed)):
        color = Adafruit_WS2801.RGB_to_color(0, math.floor(255/divisor), math.floor(math.floor(i*speed)/divisor))
        for j in range(pixels.count()):
            pixels.set_pixel(j, color)
        pixels.show()
        if wait > 0:
            time.sleep(wait)
    for i in range(math.floor(256/speed)):
        color = Adafruit_WS2801.RGB_to_color(0, math.floor((255-math.floor(i*speed))/divisor), math.floor(255/divisor))
        for j in range(pixels.count()):
            pixels.set_pixel(j,color)
        pixels.show()
        if wait > 0:
            time.sleep(wait)
    for i in range(math.floor(256/speed)):
        color = Adafruit_WS2801.RGB_to_color(math.floor((math.floor(i*speed))/divisor), 0, math.floor(255/divisor))
        for j in range(pixels.count()):
            pixels.set_pixel(j,color)
        pixels.show()
        if wait > 0:
            time.sleep(wait)
    for i in range(math.floor(256/speed)):
        color = Adafruit_WS2801.RGB_to_color(math.floor(255/divisor), 0, math.floor((255-math.floor(i*speed))/divisor))
        for j in range(pixels.count()):
            pixels.set_pixel(j,color)
        pixels.show()
        if wait > 0:
            time.sleep(wait)
