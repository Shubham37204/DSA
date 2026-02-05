# def isSafe(board, row, col, n):
#     # check row
#     for j in range(n):
#         if board[row][j] == 'Q':
#             return False

#     # check column
#     for i in range(n):
#         if board[i][col] == 'Q':
#             return False

#     # upper-left diagonal
#     i, j = row, col
#     while i >= 0 and j >= 0:
#         if board[i][j] == 'Q':
#             return False
#         i -= 1
#         j -= 1

#     # upper-right diagonal
#     i, j = row, col
#     while i >= 0 and j < n:
#         if board[i][j] == 'Q':
#             return False
#         i -= 1
#         j += 1

#     return True


# def nQueen(board, row, n, ans):
#     if row == n:
#         ans.append(board.copy())   
#         return

#     for j in range(n):
#         if isSafe(board, row, j, n):
#             board[row] = board[row][:j] + 'Q' + board[row][j+1:]
#             nQueen(board, row + 1, n, ans)
#             board[row] = board[row][:j] + '.' + board[row][j+1:]

# n=4
# board = ['.' * n for _ in range(n)] #['....', '....', '....', '....']
# ans = []
# nQueen(board,0,4,ans)
# print(ans)


from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def isSafe(board, row, col, n):

            # check row IE HORIZONTALLY
            for j in range(n):
                if board[row][j] == 'Q':
                    return False

            # check column IE VERTICALLY
            for i in range(n):
                if board[i][col] == 'Q':
                    return False

            # upper-left diagonal IE LEFT DIAGONAL
            i, j = row, col
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            # upper-right diagonal IE RIGHT DIAGONAL
            i, j = row, col
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            return True


        def nQueen(board, row, n, ans):
            if row == n:
                ans.append(board.copy())
                return

            for j in range(n):
                if isSafe(board, row, j, n):
                    board[row] = board[row][:j] + 'Q' + board[row][j+1:]
                    nQueen(board, row + 1, n, ans)
                    board[row] = board[row][:j] + '.' + board[row][j+1:]

        board = ['.' * n for _ in range(n)]
        ans = []
        nQueen(board, 0, n, ans)
        return ans
