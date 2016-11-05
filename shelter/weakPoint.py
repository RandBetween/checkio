def weak_point(matrix):
    row_sum = [sum(list) for list in matrix]
    col_sum = [sum([matrix[x][y] for x in range(len(matrix))]) for y in range(len(matrix))]
    return (row_sum.index(min(row_sum)), col_sum.index(min(col_sum)))
