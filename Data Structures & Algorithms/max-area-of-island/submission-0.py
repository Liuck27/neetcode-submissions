class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ROWS,COLS = len(grid), len(grid[0])

        def get_n(coord):
            res=[]
            row,col = coord
            d_row = [-1,0,1,0]
            d_col = [0,-1,0,1]
            for i in range(len(d_row)):
                r = row + d_row[i]
                c = col + d_col[i]
                if 0<=r<ROWS and 0<=c<COLS:
                    res.append((r,c))
            return res

        def dfs(coord):
            row,col = coord
            if grid[row][col] == 0:
                return 0 
            #we have to count this cell
            grid[row][col] = 0
            count = 1
            for n in get_n(coord):
                nr,nc = n
                if grid[nr][nc] == 1:
                    count += dfs(n)
            return count

        max_Area = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    area = dfs((r,c))
                    max_Area = max(max_Area,area)

        return max_Area
        