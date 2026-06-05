"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        res = []

        for inter in intervals:
            res.append((inter.start,inter.end))

        res.sort()

        for i in range(len(res)-1):
            if res[i][1] > res[i+1][0]:
                return False

        return True
        


