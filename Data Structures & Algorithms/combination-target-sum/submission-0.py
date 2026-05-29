class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        def backtrack(index, path):
            if sum(path) == target:
                res.append(path[:])
                return
            elif sum(path) > target or index >=len(nums):
                return
            
            path.append(nums[index])
            backtrack(index, path)
            path.pop()
            backtrack(index+1, path)

        backtrack(0,[])
        return res
        