def checkio(x):
    x.sort()
    if (len(x)%2) != 0:
        return float(x[len(x)//2])
    else:
        return (x[(len(x)//2)-1] + x[len(x)//2])/2.0
