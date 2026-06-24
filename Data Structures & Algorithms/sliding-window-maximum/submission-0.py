class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res = []

        for l in range(len(nums)-k+1):
            res.append(max(nums[l:l+k]))

        return res

        