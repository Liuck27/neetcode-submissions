class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ROWS, COLS = len(matrix), len(matrix[0])
        l,r= 0, ROWS-1
        row = 0
        while l<=r:
            row = (l+r) // 2

            if matrix[row][0] <= target <= matrix[row][-1]:
                break
            elif matrix[row][0] > target:
                r = row - 1
            elif matrix[row][-1] < target:
                l = row +1 
            else:
                return False
        
        l,r= 0, COLS-1

        while l<=r:
            mid = (l+r) // 2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid +1
            else:
                r = mid -1
        
        return False
            
                
        