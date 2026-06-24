class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = defaultdict(int)

        def dfs(money):
            if money == 0:
                return 0
            if money in memo:
                return memo[money]

            minN = amount + 1
            for coin in coins:
                if money - coin >= 0:
                    minN = min(minN, 1 + dfs(money - coin))
            memo[money] = minN
            return minN
        
        res = dfs(amount)
        if res == amount + 1:
            return -1
        return res
