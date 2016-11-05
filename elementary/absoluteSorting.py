def checkio(numbers_array):
    return sorted(numbers_array, cmp=lambda x,y: cmp(abs(x), abs(y)))
