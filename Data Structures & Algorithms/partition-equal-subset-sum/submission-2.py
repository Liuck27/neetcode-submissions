class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        if total % 2 == 1:
            return False

        goal = total / 2

        memo = {}

        def dfs(i,goal):
            if goal - nums[i ]== 0:
                return True
            
            res = False
            for j in range(i+1,len(nums)):
                res = res or dfs(j, goal - nums[i])
            return res

        return dfs(0,goal)

        