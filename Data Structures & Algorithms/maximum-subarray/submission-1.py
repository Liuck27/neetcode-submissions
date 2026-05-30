class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if not nums:
            return None

        i,j = 0 ,0

        maxS = nums[0]
        curr = 0

        while j<len(nums) and i<len(nums):
            curr +=nums[j]
            maxS = max(maxS,curr)
            if curr>0:
                j +=1
            else:
                curr = 0
                i = j+1
                j = i
        return maxS
            