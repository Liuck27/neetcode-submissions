class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        hashm = set()

        for num in nums:
            if num in hashm:
                return num
            else:
                hashm.add(num)
        