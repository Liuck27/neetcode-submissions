class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1
        last = nums[-1]

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > last:
                l = mid + 1
            else:
                r = mid - 1

        cutoff = l

        if target <= last:
            r = len(nums) - 1
        else:
            r = l - 1
            l = 0

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1
