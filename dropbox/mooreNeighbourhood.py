def count_neighbours(grid, row, col):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (row + i) >= 0 and (row + i) <= (len(grid)-1) and (col + j) >= 0 and (col + j) <= (len(grid[0])-1):
                count += grid[row + i][col + j]
    return count - grid[row][col]
