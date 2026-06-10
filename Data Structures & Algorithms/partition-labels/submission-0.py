class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        d = defaultdict(int)

        for i,c in enumerate(s):
            d[c] = i
        
        size = 0
        res = []
        end = 0
        for i,c in enumerate(s):
            end = max(end,d[c])
            size += 1
            if end == i:
                res.append(size)
                size = 0
                
        return res



        