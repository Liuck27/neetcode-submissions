class Solution:
    from collections import Counter
    import heapq
    def leastInterval(self, tasks: List[str], n: int) -> int:

        t = 0
        map = Counter(tasks)

        freq = [-count for count in map.values()]

        heapq.heapify(freq)
        que = []

        while freq or que:
            if que:
                elem = que[0]
                if elem[1] <t:
                    heapq.heappush(freq,que.pop(0)[0])

            if freq:
                elem = heapq.heappop(freq)
                elem +=1
                if elem != 0:
                    que.append([elem, t+n])
            t +=1
            
        return t


        

        