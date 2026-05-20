class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxP = 0

        l = 0
        r = l+1

        while r < len(prices):
            if prices[r]-prices[l] > maxP:
                maxP = prices[r]-prices[l]
            
            if prices[r] < prices[l]:
                l=r
                r +=1
            else:
                r +=1

        return maxP
        