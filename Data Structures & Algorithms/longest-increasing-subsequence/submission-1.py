class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        memo = {}

        def dfs(i):

            if i == len(nums)-1:
                return 1
            
            if i in memo:
                return memo[i]

            maxL = 1
            for j in range(i+1,len(nums)):
                if nums[j] > nums[i]:
                    maxL = max(maxL,1 + dfs(j))
            
            memo[i] = maxL
            return maxL

            
        maxElem = 0
        for i in range(len(nums)):
            maxElem = max(maxElem, dfs(i))


        return maxElem
        