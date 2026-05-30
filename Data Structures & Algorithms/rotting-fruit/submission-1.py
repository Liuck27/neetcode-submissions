class Solution:
    from collections import deque
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid), len(grid[0])
        def get_n(coord):
            row,col = coord
            res = []
            d_r = [-1,0,1,0]
            d_c = [0,-1,0,1]
            for i in range(len(d_r)):
                r,c = row+d_r[i], col+d_c[i]
                if 0<=r<ROWS and 0<=c<COLS:
                    res.append((r,c))
            return res

        queue = deque()

        mins = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==2:
                    queue.append(((r,c),0))

        while len(queue)>0:
            cell,dist = queue.popleft()
            mins = max(mins,dist)
            for n in get_n((cell)):
                nr,nc = n
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append(((nr,nc),dist+1))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    return -1


        return mins



        
        