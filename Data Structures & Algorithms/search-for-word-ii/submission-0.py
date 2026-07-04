class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        self.index = -1


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = TrieNode()
        res = []
        N, M = len(board), len(board[0])

        # Populate Trie
        for i, word in enumerate(words):
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.endOfWord = True
            node.index = i

        def get_N(coords):
            result = []
            r, c = coords
            d_r = [-1, 0, 1, 0]
            d_c = [0, -1, 0, 1]
            for i in range(4):
                row = r + d_r[i]
                col = c + d_c[i]
                if 0 <= row < N and 0 <= col < M:
                    result.append((row, col))
            return result

        visited = set()

        def dfs(cell, i, node):
            if node.endOfWord and node.index >= 0:
                res.append(words[node.index])
                node.index = -1
            visited.add(cell)
            for r, c in get_N(cell):
                if board[r][c] in node.children and (r,c) not in visited:
                    dfs((r, c), i + 1, node.children[board[r][c]])
            visited.discard(cell)

        # Scan the board
        for row in range(N):
            for col in range(M):
                if board[row][col] in root.children:
                    dfs((row, col), 0, root.children[board[row][col]])

        return res
