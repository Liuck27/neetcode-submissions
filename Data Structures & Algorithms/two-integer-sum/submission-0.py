class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        my_map = {}

        for i,num in enumerate(nums):
            complement = target - num
            if complement in my_map:
                return [my_map[complement], i]

            if num not in my_map:
                my_map[num] = i
            
        return []
            

        