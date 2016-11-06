def greatest_common_divisor(*args):
    args = list(args)
    args.sort()
    GCD = args[0]
    for i in range(len(args) - 1):
            GCD = GCD_Sub(args[0], args[i+1])
            args[0] = GCD
    return GCD

def GCD_Sub(a, b):
    list = [a, b]
    list.sort()
    if list[1]%list[0] == 0:
        return list[0]
    return GCD_Sub(list[0], list[1]%list[0])
