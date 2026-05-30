class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        def get_n(coord):
            res = []
            row,col = coord

            delta_row = [-1,0,1,0]
            delta_col = [0,-1,0,1]

            for i in range(len(delta_row)):
                r = row + delta_row[i]
                c = col + delta_col[i]
                if 0<=r<ROWS and 0<=c<COLS:
                    res.append((r,c))
            return res

        def dfs(coord):
            row,col = coord
            if grid[row][col] == "0":
                return
            else:
                grid[row][col] = "0"
                for n in get_n(coord):
                    nr,nc = n
                    if grid[nr][nc]=="1":
                        dfs(n)

        count = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=="1":
                    count +=1
                    dfs((r,c))

        return count
        

