class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 1)]

        #parto dalla fine 
        for i in range(n - 1, -1, -1):
            for buying in [True, False]:
                # If i can buy:
                if buying:
                    #Oggi compro - prices[i] ma quindi da domani sto vendendo dp[i + 1][False]
                    buy = dp[i + 1][False] - prices[i] if i + 1 < n else -prices[i]
                    #Oggi non compro, quindi il max profit è uguale a quello di domani dp[i + 1][True]
                    hold = dp[i + 1][True] if i + 1 < n else 0
                    dp[i][1] = max(buy, hold)
                else:
                    # Oggi vendo e incasso prices[i], ma fra 2 giorni posso ricomprare dp[i + 2][True]
                    sell = dp[i + 2][True] + prices[i] if i + 2 < n else prices[i]
                    # Oggi hold, posso vendere domani
                    hold = dp[i + 1][False] if i + 1 < n else 0
                    dp[i][0] = max(sell, hold)

        return dp[0][1]