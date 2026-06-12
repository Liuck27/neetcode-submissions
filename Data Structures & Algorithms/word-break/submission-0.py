class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        memo = {}

        def dfs(s):
            if len(s) == 0:
                return True
            if s in memo:
                return memo[s]

            res = False
            for word in wordDict:
                if s.startswith(word):
                    res = res or dfs(s[len(word):])

            memo[s] = res
            return res

        return dfs(s)
        