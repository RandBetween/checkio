def checkio(*args):
    float_list = list(args)
    try:
        return max(float_list) - min(float_list)
    except ValueError:
        return 0
