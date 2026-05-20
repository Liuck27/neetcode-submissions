import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def is_okay(piles,h,k):
            tot = 0
            for pile in piles:
                tot += math.ceil(pile/k) 
            return tot <=h

        l=1
        r = max(piles)
        K = r
        while l<=r:
            mid = (l+r) // 2
            if is_okay(piles,h,mid):
                K = mid
                r = mid -1
                
            else:
                l = mid +1 
        
        return K
        