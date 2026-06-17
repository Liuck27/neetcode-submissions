class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        N, M = len(heights), len(heights[0])
        pacific = [[False for _ in range(M)] for _ in range(N)]
        atlantic = [[False for _ in range(M)] for _ in range(N)]

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

        def dfsp(coords):
            row, col = coords
            pacific[row][col] = True
            
            for r,c in getN(coords):
                if heights[r][c] >= heights[row][col] and not pacific[r][c]:
                    dfsp((r,c))

        def dfsa(coords):
            row, col = coords
            atlantic[row][col] = True
            
            for r,c in getN(coords):
                if heights[r][c] >= heights[row][col] and not atlantic[r][c]:
                    dfsa((r,c))
            
        for i in range(N):
            dfsp((i,0))
            dfsa((i,M-1))

        for i in range(M):
            dfsp((0,i))
            dfsa((N-1,i))

        res = []
        for i in range(N):
            for j in range(M):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i,j])
        return res
