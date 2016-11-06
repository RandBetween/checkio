def super_root(number):
    a, b = float(0), min(float(number), float(10))
    m = (a + b) / float(2)
    functionM = m ** m
    while (abs(functionM - number) > .001):
        m = (a + b) / float(2)
        functionM = m ** m
        if (functionM - number) < 0:
            a = m
        else:
            b = m
    return m

print super_root(27)
print super_root(81)
print super_root(4)
print super_root(10000000000)
