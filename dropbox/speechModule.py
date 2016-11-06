dict = {
    0 : "",
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
}
​
dict2 = {
    10 : "ten",
    11 : "eleven",
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen",
    15 : "fifteen",
    16 : "sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "nineteen",
}
​
dict3 = {
    0 : "",
    2 : "twenty",
    3 : "thirty",
    4 : "forty",
    5 : "fifty",
    6 : "sixty",
    7 : "seventy",
    8 : "eighty",
    9 : "ninety",
}
​
dict4 = {
    1 : "one hundred",
    2 : "two hundred",
    3 : "three hundred",
    4 : "four hundred",
    5 : "five hundred",
    6 : "six hundred",
    7 : "seven hundred",
    8 : "eight hundred",
    9 : "nine hundred",
}
​
def checkio(n):
    str_n = str(n)
    if n < 10:
        return dict[n]
    elif n < 20:
        return dict2[n]
    elif n < 100:
        result = dict3[int(str_n[0])] + " " + dict[int(str_n[1])]
        return result.strip()
    elif n < 1000 and str_n[1] == str(1):
        return dict4[int(str_n[0])] + " " + dict2[int(str_n[1:3])]
    elif n < 1000 and str_n[1] == str(0):
        result = dict4[int(str_n[0])] + " " + dict[int(str_n[2])]
        return result.strip()
    else:
        result = dict4[int(str_n[0])] + " "  + dict3[int(str_n[1])] + " " + dict[int(str_n[2])]
        return result.strip()
