from __init__ import *
def serialized_hue_shift(wait, speed,divisor):
    pixels.clear()
    pixels.show()
    time.sleep(2)
    color_list = []

    # Generate the colors
    for i in range(int(math.floor(256/speed))):
        # color = Adafruit_WS2801.RGB_to_color(0, int(math.floor(255/divisor)), int(math.floor(math.floor(i*speed)/divisor)))
        color = RGB_to_color(0,255,i*speed,divisor)
        color_list.append(color)
    for i in range(int(math.floor(256/speed))):
        # color = Adafruit_WS2801.RGB_to_color(0, int(math.floor((255-math.floor(i*speed))/divisor)), int(math.floor(255/divisor)))
        color = RGB_to_color(0,255-(i*speed),255,divisor)
        color_list.append(color)
    for i in range(int(math.floor(256/speed))):
        # color = Adafruit_WS2801.RGB_to_color(int(math.floor(math.floor(i*speed)/divisor)), 0, int(math.floor(255/divisor)))
        color = RGB_to_color(i*speed,0,255,divisor)
        color_list.append(color)
    for i in range(int(math.floor(256/speed))):
        # color = Adafruit_WS2801.RGB_to_color(int(math.floor(255/divisor)), 0, int(math.floor((255-math.floor(i*speed))/divisor)))
        color = RGB_to_color(255,0,255-(i*speed),divisor)
        color_list.append(color)

    #Light the LEDs
    for i in range(len(color_list)+1):
        for j in range(pixels.count()): 
            k = (i+j)%len(color_list) #if we exceed the list, wrap around
            pixels.set_pixel(j, color_list[k])
        pixels.show()
        if wait > 0:
            time.sleep(wait)
