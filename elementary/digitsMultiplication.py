def checkio(number):
    return reduce(lambda x, y: x*y, [int(x) for x in list(str(number)) if int(x) != 0])
