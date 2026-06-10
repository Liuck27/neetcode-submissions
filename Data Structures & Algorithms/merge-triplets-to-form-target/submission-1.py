class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        def checkGreater(triplet,t):
            for i in range(len(triplet)):
                if triplet[i] > t[i]:
                    return True
            return False

        def merge(t1,t2):
            t = []
            for i in range(len(t1)):
                t.append(max(t1[i],t2[i]))
            return t 
                
        res = [0,0,0]
        for i in range(len(triplets)):
            if not checkGreater(triplets[i],target):
                res = merge(triplets[i],res)
            
        return res == target

        