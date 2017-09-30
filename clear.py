import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI

PIXEL_COUNT = 160

PIXEL_CLOCK = 11
PIXEL_DOUT = 10

pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, clk=PIXEL_CLOCK, do=PIXEL_DOUT)

pixels.clear()

pixels.show()
