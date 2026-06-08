class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        grid = [[1 for i in range(m)] for j in range(n)]

        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

        return grid[-1][-1]
