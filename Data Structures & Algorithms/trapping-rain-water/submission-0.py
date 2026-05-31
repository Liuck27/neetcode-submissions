class Solution:
    def trap(self, height: List[int]) -> int:

        pre = [0] * len(height)
        post = [0] * len(height)

        pre[0] = height[0]
        for i in range(1, len(height)):
            pre[i] = max(pre[i - 1], height[i])

        post[len(height) - 1] = height[len(height) - 1]
        for i in range(len(height) - 2, -1, -1):
            post[i] = max(post[i + 1], height[i])

        water = 0
        for i in range(len(height)):
            water += min(pre[i], post[i]) - height[i]

        return water
