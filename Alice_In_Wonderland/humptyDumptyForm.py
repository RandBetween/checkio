import math

def checkio(height, width):
    c = height / 2.0
	a = width / 2.0

	result = [round(volume(c, a), 2), round(surface_area(c, a), 2)]
	return result

def surface_area(c, a):
	if c < a:
		e_squared = (1 - (c**2/a**2))
		e = math.sqrt(e_squared)
		return (2*math.pi*a**2)*(1+(((1-e_squared)/e)*(math.atanh(e))))
	elif c > a:
		e_squared = (1 - (a**2/c**2))
		e = math.sqrt(e_squared)
		return (2*math.pi*a**2)*(1+((c)/(a*e))*(math.asin(e)))
	else:
		return 4*math.pi*c**2

def volume(c, a):
	return ((4*math.pi)/3)*a**2*c
