class Solution:
    def climbStairs(self, n: int) -> int:

        prev = 0
        curr = 1


        for elem in range(1,n+1):
            temp = curr
            curr = curr + prev
            prev = temp
        
        return curr
            
        