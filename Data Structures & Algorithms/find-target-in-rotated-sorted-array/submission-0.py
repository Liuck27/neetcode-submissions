class Solution:
    def search(self, nums: List[int], target: int) -> int:

        cut = -1

        l,r = 0, len(nums)-1

        while l<=r:
            mid = (l+r) //2

            if nums[mid] <= nums[-1]:
                cut = mid
                r = mid - 1
            else:
                l = mid + 1

        if target > nums[-1]:
            l = 0
            r = cut
        else:
            l = cut
            r = len(nums) - 1

        while l<=r:
            mid = (l+r) //2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1
        

        