def checkio(data):
    new_matrix = []
    for i in range(len(data[0])):
        new_list = []
        for j in range(len(data)):
            new_list.append(data[j][i])
        new_matrix.append(new_list)
    return new_matrix
