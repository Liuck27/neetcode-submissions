class Solution:
    def solve(self, board: List[List[str]]) -> None:

        N, M = len(board), len(board[0])
        visited = set()

        def dfs(i, j):
            if i < 0 or j < 0 or i >= N or j >= M or (i, j) in visited or board[i][j] == "X":
                return
            visited.add((i, j))

            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        for i in range(N):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][M - 1] == "O":
                dfs(i, M - 1)

        for i in range(M):
            if board[0][i] == "O":
                dfs(0, i)
            if board[N-1][i] == "O":
                dfs(N - 1, i)

        for i in range(N):
            for j in range(M):
                if (i, j) not in visited:
                    board[i][j] = "X"
