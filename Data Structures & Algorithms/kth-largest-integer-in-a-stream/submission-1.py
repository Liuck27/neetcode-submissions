class KthLargest:
    import heapq

    def __init__(self, k: int, nums: List[int]):

        self.data, self.k = nums, k
        
        heapq.heapify(self.data)
        while len(self.data)>self.k:
            heapq.heappop(self.data)

        

    def add(self, val: int) -> int:
        heapq.heappush(self.data,val)
        if len(self.data)>self.k:
            heapq.heappop(self.data)

        return self.data[0]
        
