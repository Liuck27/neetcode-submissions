class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        dictlist = [set() for _ in range(27)]
        ROWS = COLS = 9

        for i,row in enumerate(board):
            for j, elem in enumerate(row):

                if elem == ".":
                    continue

                if elem in dictlist[i]:
                    return False
                else:
                    dictlist[i].add(elem)

                if elem in dictlist[COLS+j]:
                    return False
                else:
                    dictlist[COLS+j].add(elem)

                if elem in dictlist[ROWS+COLS+((i//3)*3+(j//3))]:
                    return False
                else:
                    dictlist[ROWS+COLS+((i//3)*3+(j//3))].add(elem)                    


        return True

        

        