class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        from collections import defaultdict

        hmap = defaultdict(int)

        for i, num in enumerate(nums):
            complem = target - num 
            if complem in hmap:
                return [hmap[complem], i]
            hmap[num] = i
            


