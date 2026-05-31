class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        hset = set(nums)
        longest = 0

        for num in hset:

            if num-1 not in hset:
                i = 0
                while num+i in hset: 
                    i +=1
                longest = max(longest,i)

        return longest