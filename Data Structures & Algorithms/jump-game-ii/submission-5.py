class Solution:
    def jump(self, nums: List[int]) -> int:

        l,r = 0,0
        N = len(nums)
        cnt = 0

        while r<N-1:
            maxR = 0
            for i in range(l,r+1):
                maxR = max(maxR,i+nums[i])
            l = r+1 
            r = maxR
            cnt +=1

        return cnt


