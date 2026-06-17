class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        N, M = len(grid), len(grid[0])

        def getN(coords):
            r, c = coords
            res = []
            d_r = [-1, 0, 1, 0]
            d_c = [0, -1, 0, 1]
            for i in range(4):
                row = r + d_r[i]
                col = c + d_c[i]
                if 0 <= row < N and 0 <= col < M:
                    res.append((row, col))

            return res

        queue = deque()
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 0:
                    queue.append([(i, j), 0])

        while queue:
            cell = queue.popleft()
            row, col = cell[0]
            dist = cell[1]
            grid[row][col] = min(dist,grid[row][col])

            for r, c in getN((row, col)):
                if grid[r][c] == 2147483647:
                    queue.append([(r, c), dist + 1])
