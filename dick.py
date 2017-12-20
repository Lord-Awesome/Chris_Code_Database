from __init__ import *

def dick():

	print("In dick...")

	pixels.clear()
	pixels.show()

	divisor = 4
	dick_color = [RGB_to_color(0,255,0,divisor),RGB_to_color(255,0,0,divisor),RGB_to_color(255,50,255,divisor),RGB_to_color(0,0,255,divisor),RGB_to_color(255,50,255,divisor)]

	off_color = RGB_to_color(0,0,0,1)

	dick = [[0,6],[0,7],[0,8],[1,5],[1,7],[1,9],[2,4],[2,7],[2,10],[3,4],[3,10],[4,4],[4,10],[5,4],[5,10],[6,4],[6,10],[7,2],[7,3],[7,4],[7,10],[7,11],[7,12],[8,2],[8,3],[8,4],[8,10],[8,11],[8,12],[9,2],[9,3],[9,4],[9,10],[9,11],[9,12]]
	
	t = 0

	while (t<1):

		for i in range(10):
			for j in range(16):
				index = [i,j]

				if index in dick:
					pixels.set_pixel((index[0]*16)+index[1], dick_color[0])
					pixels.show()

				else:
					pixels.set_pixel((index[0]*16)+index[1], dick_color[1])
					pixels.show()
					pixels.set_pixel((index[0]*16)+index[1], off_color)
					pixels.show()


		t += 1

