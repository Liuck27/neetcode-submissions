class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxprofit = 0

        l = 0
        r = l + 1

        while r < len(prices):
            profit = prices[r] - prices[l]

            maxprofit = max(maxprofit, profit)
            if prices[r] < prices[l]:
                l = r
                r = l + 1
            else:
                r += 1

        return maxprofit
