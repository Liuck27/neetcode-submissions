class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0
        if len(nums)<3:
            return max(nums)
        if len(nums) == 3:
            return max(nums[1],nums[0] + nums[2] )

        money = [0] * len(nums)
        money[0:2] = nums[0:2]
        money[2] = nums[0] + nums[2]

        for i in range(3, len(nums)):
            money[i] = nums[i] + max(money[i-2], money[i-3])

        return max(money)

        