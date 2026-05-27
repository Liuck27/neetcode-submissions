class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        res = []

        for point in points:
            dist = point[0]**2 + point[1]**2
            res.append((dist, point))

        res = heapq.nsmallest(k,res)
        return [p[1] for p in res]
        