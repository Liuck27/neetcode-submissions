class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        t = nums[0]
        for num in nums[1:]:
            t = t ^ num

        return t
