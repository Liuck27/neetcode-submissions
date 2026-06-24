class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res = []
        heap = []
        heapq.heapify(heap)

        for i in range(k-1):
            heapq.heappush(heap,(-nums[i], i))

        for r in range(k-1, len(nums)):
            heapq.heappush(heap,(-nums[r], r))
            while heap[0][1] < r-k+1:
                heapq.heappop(heap)
            res.append(-heap[0][0])

    
        return res
