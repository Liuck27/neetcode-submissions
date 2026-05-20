class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        res = 0
        for num in range(len(nums)):
            res = (res^num+1)^nums[num]
        
        return res



        