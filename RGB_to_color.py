def RGB_to_color(R,B,G,divisor):
	return(Adafruit_WS2801.RGB_to_color(int(math.floor(R/divisor)),int(math.floor(B/divisor)),int(math.floor(G/divisor))))