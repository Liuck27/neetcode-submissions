class Solution:
    from collections import deque
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
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
        
        def bfs():
            while len(queue)>0:
                row,col = queue.popleft()
                #if water skip
                if grid[row][col] == -1:
                    continue
                for n in get_n((row,col)):
                    nr,nc = n
                    if grid[nr][nc] == 2147483647:
                        grid[nr][nc] = grid[row][col]+1
                        queue.append(n)

        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==0:
                    queue.append((r,c))

        bfs()

        return 

