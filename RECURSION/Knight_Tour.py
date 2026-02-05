def isValid(grid, row, col, n, expectedValue):
    # base case
    if row < 0 or col < 0 or row >= n or col >= n or grid[row][col] != expectedValue:
        return False
    if expectedValue == n*n-1:
        return True

    ans1 = isValid(grid, row+2, col+1, n, expectedValue+1)
    ans2 = isValid(grid, row+1, col+2, n, expectedValue+1)
    ans3 = isValid(grid, row-1, col+2, n, expectedValue+1)
    ans4 = isValid(grid, row-2, col+1, n, expectedValue+1)
    ans5 = isValid(grid, row-2, col-1, n, expectedValue+1)
    ans6 = isValid(grid, row-1, col-2, n, expectedValue+1)
    ans7 = isValid(grid, row+1, col-2, n, expectedValue+1)
    ans8 = isValid(grid, row+2, col-1, n, expectedValue+1)
    return ans1 or ans2 or ans3 or ans4 or ans5 or ans6 or ans7 or ans8


grid = [[0, 11, 16, 5, 20],
        [17, 4, 19, 10, 15],
        [12, 1, 8, 21, 6],
        [3, 18, 23, 14, 9],
        [24, 13, 2, 7, 22]]
s = len(grid)
print(isValid(grid, 0, 0, s, 0))
