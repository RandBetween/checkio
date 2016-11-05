def checkio(array):
    if len(array) == 0:
		return 0
	else:
		return sum([array[x] for x in range(len(array)) if x % 2 == 0])*array[len(array)-1]
