class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if not nums:
            return None

        j = 0 
        maxS = nums[0]
        curr = 0

        while j<len(nums):
            curr +=nums[j]
            maxS = max(maxS,curr)
            if curr>0:
                j +=1
            else:
                curr = 0
                j +=1
                
        return maxS
            