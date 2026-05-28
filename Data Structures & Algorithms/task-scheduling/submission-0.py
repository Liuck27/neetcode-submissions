class Solution:
    from collections import defaultdict
    import heapq
    def leastInterval(self, tasks: List[str], n: int) -> int:

        t = 0
        map = defaultdict(int)
        for elem in tasks:
            map[elem] -=1

        freq = [[count,task] for task,count in map.items()]
        for item in freq:
            item.append(0)

        heapq.heapify(freq)
        que = []

        while freq or que:
            if que:
                elem = que[0]
                if elem[2] <t:
                    heapq.heappush(freq,que.pop(0))

            if freq:
                elem = heapq.heappop(freq)
                elem[0] +=1
                elem[2] = t+n
                if elem[0] != 0:
                    que.append(elem)
            t +=1
            
        return t


        

        