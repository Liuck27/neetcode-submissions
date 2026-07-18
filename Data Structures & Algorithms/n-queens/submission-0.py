class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        board = [["."] * n for _ in range(n)]
        result = []

        def is_valid(row, col):
            # Check row
            for i in range(col):
                if board[row][i] == "Q":
                    return False
            # Check diagonals
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1

            i, j = row + 1, col - 1
            while i < n and j >= 0:
                if board[i][j] == "Q":
                    return False
                i += 1
                j -= 1

            return True

        def backtrack(col):
            if col == n:
                out = ["".join(r) for r in board]
                result.append(out)
                return
            for row in range(n):
                board[row][col] = "Q"
                if is_valid(row, col):
                    backtrack(col + 1)
                board[row][col] = "."

        backtrack(0)
        return result
