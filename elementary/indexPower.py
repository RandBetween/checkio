def index_power(array, n):
    try:
        return array[n]**n
    except IndexError:
        return -1
