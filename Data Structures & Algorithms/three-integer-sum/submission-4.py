class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []

        i = 0
        while i<len(nums)-2:
            target = -nums[i]
            j=i+1
            k= len(nums)-1

            while j<k:
                if nums[j]+nums[k] == target:
                    res.append([nums[i],nums[j],nums[k]])
                    while j<k and nums[j] == nums[j+1]:
                        j +=1
                    while j<k and nums[k] == nums[k-1]:
                        k -=1
                    j +=1
                    k -=1
                elif nums[j]+nums[k] < target:
                    j +=1
                else:
                    k-=1
            while i<len(nums)-2 and nums[i] == nums[i+1]:
                i +=1
            i+=1

        return res




        