import math

def checkio(a, b, c):
    if is_triangle(a, b, c):
		cosA = (float(b)**2 + float(c)**2 - float(a)**2)/(2*float(b)*float(c))
		cosB = (float(c)**2 + float(a)**2 - float(b)**2)/(2*float(c)*float(a))
		A = round(math.degrees((math.acos(cosA))))
		B = round(math.degrees((math.acos(cosB))))
		C = 180 - A - B
		result = [int(A), int(B), int(C)]
		result.sort()
		return result
	return [0, 0, 0]


def is_triangle(a, b, c):
		list = [a, b, c]
		list.sort()
		if list[0]+list[1] > list[2]:
			return True
		return False
