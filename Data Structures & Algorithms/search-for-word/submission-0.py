class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        N, M = len(board), len(board[0])
        hashset = set()

        def get_neigh(row, col):
            res = []
            d_row = [-1, 0, 1, 0]
            d_col = [0, -1, 0, 1]
            for i in range(4):
                r = row + d_row[i]
                c = col + d_col[i]
                if 0 <= r < N and 0 <= c < M:
                    res.append((r, c))
            return res

        def backtracking(x, y, i):
            # Se siamo arrivati alla fine della parola, l'abbiamo trovata!
            if i == len(word):
                return True
            
            hashset.add((x, y))
            
            # Esploriamo i vicini
            for n_x, n_y in get_neigh(x, y):
                if (n_x, n_y) not in hashset and board[n_x][n_y] == word[i]:
                    # Se una qualsiasi delle strade future restituisce True, propagalo in alto
                    if backtracking(n_x, n_y, i + 1):
                        return True
            
            # Backtracking: ripuliamo il set per i prossimi tentativi
            hashset.discard((x, y))
            return False

        # Punto di partenza: cerchiamo la prima lettera della parola nella matrice
        for i in range(N):
            for j in range(M):
                if board[i][j] == word[0]:
                    # Avviamo il backtracking dal secondo carattere (indice 1)
                    if backtracking(i, j, 1):
                        return True
                        
        return False