class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # for i in range(len(intervals)):
        #     if newInterval[0] > intervals[i][0]:
        #         intervals.insert(i+1,newInterval)
        #         break

        i = 0
        while i<len(intervals) and newInterval[0] > intervals[i][0]:
            i += 1
        
        #lo inserisco al posto giusto poi sistemi gli intervalli
        intervals.insert(i, newInterval)

        #ora devo aggiustare l'end del newInterval se si sovrappone con quelli successivi
        j = 0
        while i+1+j < len(intervals) and intervals[i][1] >= intervals[i+1+j][0]:
            j += 1
        intervals[i][1] = max(intervals[i][1],intervals[i+j][1])
        intervals[i + 1 : i + 1 + j] = []


        #il nuovo intervallo si sovrappone a quello precedente
        if i>0 and intervals[i][0] <= intervals[i - 1][1]:
            intervals[i-1][1] = max(intervals[i-1][1],intervals[i][1])
            intervals.pop(i)



        return intervals
