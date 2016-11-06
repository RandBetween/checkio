def checkio(n, m):
    zipped = zip(list(bin(n)[2:].zfill(22)), list(bin(m)[2:].zfill(22)))
    return sum([1 for tuple in zipped if tuple[0] != tuple[1]])
