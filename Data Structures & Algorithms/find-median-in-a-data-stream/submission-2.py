class MedianFinder:
    def __init__(self):
        self.bottom = []
        self.top = []

    def addNum(self, num: int) -> None:
        if not self.top:
            heapq.heappush(self.top, num)
        elif num >= self.top[0]:
            heapq.heappush(self.top, num)
        else:
            heapq.heappush(self.bottom, -num)

        self.rebalance()

    def findMedian(self) -> float:
        if len(self.bottom) == len(self.top):
            return (self.top[0] - self.bottom[0]) / 2
        elif len(self.bottom) > len(self.top):
            return -self.bottom[0]
        else:
            return self.top[0]

    def rebalance(self):
        if len(self.bottom) > len(self.top) + 1:
            num = -heapq.heappop(self.bottom)
            heapq.heappush(self.top, num)
        elif len(self.bottom) + 1 < len(self.top):
            num = heapq.heappop(self.top)
            heapq.heappush(self.bottom, -num)
