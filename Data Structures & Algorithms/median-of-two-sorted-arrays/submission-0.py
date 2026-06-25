class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        m = len(nums1)
        n = len(nums2)

        res = [0] * (n + m)

        i, j = 0, 0

        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                res[i + j] = nums1[i]
                i += 1
            else:
                res[i + j] = nums2[j]
                j += 1

        while i < m:
            res[i + j] = nums1[i]
            i += 1
        while j < n:
            res[i + j] = nums2[j]
            j += 1

        l, r = 0, n + m
        mid = l + (r-l)//2
        if (n+m)%2==1:
            return res[mid]
        return (res[mid]+res[mid-1])/2


