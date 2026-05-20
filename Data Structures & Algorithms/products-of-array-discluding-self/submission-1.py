class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        N = len(nums)

        for i in range(1,N):

            prefix[i] = prefix[i-1] * nums[i-1]
            suffix[-i-1] = suffix[-i] * nums[-i]
        
        output = [0] * N

        for i in range(N):
            output[i] = prefix[i] * suffix[i]

        return output

        