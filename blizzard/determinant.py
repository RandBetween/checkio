import copy
​
def checkio(data):
    if len(data) == 1:
        return data[0][0]
    elif len(data) == 2:
        return (data[0][0]*data[1][1] - data[0][1]*data[1][0])
    result = 0
    length = len(data)
    sign = 1
    for m in range(length):
        temp_matrix = copy.deepcopy(data)
        result += sign*data[0][m]*checkio(sub_data(temp_matrix, length, m))
        sign *= -1
    return result

def sub_data(data, length, start):
    matrix = []
    for i in range(1, length):
        sub_list = data[i]
        del sub_list[start]
        matrix.append(sub_list)
    return matrix
