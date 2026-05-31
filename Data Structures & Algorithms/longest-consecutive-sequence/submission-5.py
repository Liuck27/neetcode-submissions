class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        hset = set(nums)
        curr = 0
        longest = 0

        for i in range(min(nums),max(nums)+1):

            if i in hset:
                curr +=1
                longest = max(longest,curr)
            else:
                curr = 0

        return longest