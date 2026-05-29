class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        def backtrack(path, remaining):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i,elem in enumerate(remaining):
                path.append(elem)
                backtrack(path, remaining[0:i]+remaining[i+1:])
                path.pop()



        backtrack([], nums)

        return res
        