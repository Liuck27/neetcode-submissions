class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()

        n = len(intervals) - 1
        i = 0
        while i < n:
            if intervals[i][1] < intervals[i + 1][0]:
                res.append(intervals[i])
            else:
                intervals[i + 1][0] = intervals[i][0]
                intervals[i + 1][1] = max(intervals[i][1], intervals[i + 1][1])

            i += 1
        res.append(intervals[i])

        return res
