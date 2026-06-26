class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        visited = set()
        neigh = defaultdict(set)

        for edge in edges:
            s = edge[0]
            e = edge[1]
            neigh[s].add(e)
            neigh[e].add(s)

        
        count = 0
        for key in range(n):
            if key not in visited:
                count += 1
                q = deque()
                visited.add(key)
                q.append((key, -1))

                while q:
                    node, parent = q.popleft()
                    for nei in neigh[node]:
                        if nei != parent and nei not in visited:
                            visited.add(nei)
                            q.append((nei, node))

        return count