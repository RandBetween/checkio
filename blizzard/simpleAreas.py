import math
​
def simple_areas(*args):
    if len(args) == 1:
        a = float(args[0])
        return math.pi*(a/2)**2
    elif len(args) == 2:
        a = float(args[0])
        b = float(args[1])
        return a*b
    elif len(args) == 3:
        a = float(args[0])
        b = float(args[1])
        c = float(args[2])
        s = (a + b + c)/2
        partial_answer = s*(s-a)*(s-b)*(s-c)
        answer = math.sqrt(partial_answer)
        return answer
