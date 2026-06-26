class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        # ricorsione sugli anelli partendo dall'esterno

        N, M = len(matrix), len(matrix[0])

        res = []

        r1, r2 = 0, N - 1
        c1, c2 = 0, M - 1

        while r1 <= r2 and c1 <= c2:
            row_first = [matrix[r1][j] for j in range(c1, c2 + 1)]
            row_last = [matrix[r2][j] for j in range(c2, c1 - 1, -1)] if r1 < r2 else []

            col_first = [matrix[i][c2] for i in range(r1 + 1, r2)] 
            col_last = [matrix[i][c1] for i in range(r2 - 1, r1, -1)] if c1 < c2 else []

            res += row_first + col_first + row_last + col_last

            r1 += 1
            r2 -= 1
            c1 += 1
            c2 -= 1

        return res
