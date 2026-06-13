class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        if total % 2 == 1:
            return False

        goal = total // 2

        memo = [[-1] * (goal + 1) for _ in range(len(nums) + 1)]

        def dfs(i, goal):
            if goal - nums[i] == 0:
                return True
            
            if memo[i][goal] != -1:
                return memo[i][goal]

            res = False
            for j in range(i + 1, len(nums)):
                res = res or dfs(j, goal - nums[i])
            memo[i][goal] = res
            return res

        return dfs(0, goal)
