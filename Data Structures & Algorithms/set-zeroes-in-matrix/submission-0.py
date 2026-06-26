class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        N, M = len(matrix), len(matrix[0])

        def setToZero(i: int, j: int) -> None:
            for k in range(N):
                if matrix[k][j] != "X":
                    matrix[k][j] = 0
            for k in range(M):
                if matrix[i][k] != "X":
                    matrix[i][k] = 0

        for i in range(N):
            for j in range(M):
                if matrix[i][j] == 0:
                    matrix[i][j] = "X"

        for i in range(N):
            for j in range(M):
                if matrix[i][j] == "X":
                    setToZero(i, j)

        for i in range(N):
            for j in range(M):
                if matrix[i][j] == "X":
                    matrix[i][j] = 0
