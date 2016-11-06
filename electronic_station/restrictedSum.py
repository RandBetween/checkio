def checkio(data):
    newlist = data[:1]
    if len(data) == 1:
        return newlist[0]
    else:
        return newlist[0] + checkio(data[1:])
