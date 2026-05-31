class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        N = len(nums)
        pre = [1]*N
        post = [1]*N

        for i in range(1,N):
            pre[i] = pre[i-1] * nums[i-1] 
            post[N-i-1] = post[N-i]*nums[N-i]

        res = [0] * N
        for i in range(N):
            res[i] = pre[i] * post[i]

        return res
        