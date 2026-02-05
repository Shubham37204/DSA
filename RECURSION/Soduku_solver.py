def isSafe(board, row, col, dig):
    dig = str(dig)
    for i in range(9):
        if board[row][i] == dig:
            return False

    for j in range(9):
        if board[j][col] == dig:
            return False

    srow, scol = (row//3)*3, (col//3)*3
    for i in range(srow, srow+3):
        for j in range(scol, scol+3):
            if board[i][j] == dig:
                return False
    return True

def helper(board, row, col):
    if row == 9:
        return True
    
    nextRow = row + (col + 1) // 9
    nextCol = (col + 1) % 9
    if nextCol == 9:
        nextRow = row+1
        nextCol = 0

    if board[row][col] != '.':
        return helper(board, nextRow, nextCol)

    for i in range(9):
        if isSafe(board, row, col, i):
            board[row][col] = i
            if helper(board, nextRow, nextCol):
                return True
            board[row][col] = '.'
    return False


def solveSudoku(board):
    helper(board, 0, 0)
