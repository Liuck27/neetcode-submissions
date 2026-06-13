class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        minVal = maxVal = 1   
        maxEver = nums[0]    

        for num in nums:
            temp = maxVal

            maxVal = max(maxVal*num, minVal*num, num)
            minVal = min(temp*num, minVal*num, num)

            maxEver = max(maxEver,maxVal)
        
        return maxEver
