class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        N = len(matrix)

        for j in range(N//2):
            for i in range(N):
                temp = matrix[j][i]
                matrix[j][i] = matrix[N-1-j][i]
                matrix[N-1-j][i] = temp

        for i in range(N):
            for j in range(i,N):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        
        