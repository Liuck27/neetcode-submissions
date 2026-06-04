class Solution:
    def rob(self, nums: List[int]) -> int:

        prev = 0
        curr = 0

        for house in nums:
            temp = prev
            prev = curr

            curr = max(house+temp, curr)

        return curr

        