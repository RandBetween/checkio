def checkio(number):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number_reverse = number[::-1]
    min_k = max([alphabet.index(x) for x in number]) + 1
    for k in range(min_k, 37):
        n = 0
        for i in range(len(number)):
            n += (k**i)*alphabet.index(number_reverse[i])
        if n % (k -1) == 0:
            return k
    return 0
