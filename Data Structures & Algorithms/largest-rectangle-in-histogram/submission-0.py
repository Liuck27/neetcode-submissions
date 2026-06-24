class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        def formRectangle(i):
            h = heights[i]

            l, r = i-1, i+1
            w = 1

            while l >= 0 and heights[l] >= h:
                l -= 1
                w += 1
            while r < len(heights) and heights[r] >= h:
                r += 1
                w += 1

            return w * h

        maxArea = 0
        for i in range(len(heights)):
            maxArea = max(maxArea, formRectangle(i))

        return maxArea
