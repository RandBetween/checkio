OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):
    dict = {"conjunction" : x & y, "disjunction" : x | y, "implication" : not(x) or y, "exclusive" : x ^ y, "equivalence" : int(x == y)}
    return dict[operation]
