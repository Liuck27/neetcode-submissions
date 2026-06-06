"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    import heapq
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        meetings = []

        for inter in intervals:
            meetings.append([inter.start, inter.end])

        meetings.sort()

        myheap = []

        for meeting in meetings:
            if not myheap or meeting[0]<myheap[0]:
                heapq.heappush(myheap,meeting[1])
            else:
                heapq.heappushpop(myheap,meeting[1])

        return len(myheap)




        