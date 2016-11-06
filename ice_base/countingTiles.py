import math

def checkio(radius):
	partial = 0
	solid = 0
	for i in range(5):
		for j in range(5):
			if math.sqrt(j**2 + i**2) < radius:
				partial += 1
	for i in range(5):
		for j in range(5):
			if math.sqrt((j+1)**2 + (i+1)**2) <= radius:
				solid += 1
	return [solid*4, (partial - solid)*4]
