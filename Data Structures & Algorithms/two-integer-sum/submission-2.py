class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        d = defaultdict(int)

        for i, num in enumerate(nums):
            complem = target - num
            if complem in d:
                return [d[complem], i]

            if num not in d:
                d[num] = i
