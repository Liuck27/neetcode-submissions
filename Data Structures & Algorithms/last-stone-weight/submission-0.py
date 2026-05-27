class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        import heapq
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones)>1:
            r1 = -heapq.heappop(stones)
            r2 = -heapq.heappop(stones)
            if(r1>r2):
                heapq.heappush(stones, r2-r1)
        if stones:
            return -stones[0]
        return 0
        