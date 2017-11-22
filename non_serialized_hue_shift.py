from __init__ import *
def non_serialized_hue_shift(wait, speed, divisor):

    # Generate the colors
    color_list = []
    for i in range(int(math.floor(256/speed))):
        # color = Adafruit_WS2801.RGB_to_color(0, int(math.floor(255/divisor)), int(math.floor((math.floor(i*speed))/divisor)))
        color = RGB_to_color(0,255,i*speed,divisor)
        color_list.append(color)
    for i in range(int(math.floor(256/speed))):
        # color = Adafruit_WS2801.RGB_to_color(0, int(math.floor((255-math.floor(i*speed))/divisor)), int(math.floor(255/divisor)))
        color = RGB_to_color(0,255-(i*speed),255,divisor)
        color_list.append(color)
    for i in range(int(math.floor(256/speed))):
        # color = Adafruit_WS2801.RGB_to_color(int(math.floor((math.floor(i*speed))/divisor)), 0, int(math.floor(255/divisor)))
        color = RGB_to_color(i*speed,0,255,divisor)
        color_list.append(color)
    for i in range(int(math.floor(256/speed))):
        # color = Adafruit_WS2801.RGB_to_color(int(math.floor(255/divisor)), 0, int(math.floor((255-math.floor(i*speed))/divisor)))
        color = RGB_to_color(255,0,255-(i*speed),divisor)
        color_list.append(color)
        
    pixels.clear()
    time.sleep(2)
    pixels_list = list(range(pixels.count()))
    random.shuffle(pixels_list)



    for i in range(len(color_list)+1):
        index = 0
        for j in pixels_list:
            k = (i+j)%len(color_list) #if we exceed the list, wrap around
            pixels.set_pixel(index, color_list[k])
            index = index+1
        pixels.show()
        if wait > 0:
            time.sleep(wait)
