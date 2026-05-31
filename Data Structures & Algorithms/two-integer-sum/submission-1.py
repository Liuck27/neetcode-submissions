class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        from collections import defaultdict

        d = defaultdict(int)

        for i,num in enumerate(nums):
            c = target - num
            if c in d:
                return [d[c],i]
            if num not in d:
                d[num] = i
        