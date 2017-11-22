from __init__ import *
def random_light_display(wait, speed, divisor):

    color_list = []

    # Generate the colors
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
    random.shuffle(color_list)

    for i in range(len(color_list)):
        random.shuffle(pixels_list)
        for j in pixels_list:
            k = random.randint(0, len(color_list) - 1)
            pixels.set_pixel(j, color_list[k])
        
        if (i%2 == 0):
            rand_blue = random.random()
            rand_yellow = random.random()
            if (rand_blue < 0.5):
                GPIO.output(12,GPIO.LOW)
            if (rand_yellow < 0.5):
                GPIO.output(16,GPIO.LOW)

        pixels.show()
        if wait > 0:
            time.sleep(wait)

        GPIO.output(12,GPIO.HIGH)
        GPIO.output(16,GPIO.HIGH)
