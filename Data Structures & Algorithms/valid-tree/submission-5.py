class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False

        visited = set()
        neigh = defaultdict(set)

        for edge in edges:
            s = edge[0]
            e = edge[1]
            neigh[s].add(e)
            neigh[e].add(s)

        q = deque()
        visited.add(0)
        q.append((0, -1))

        while q:
            node, parent = q.popleft()
            
            for nei in neigh[node]:
                if nei != parent:
                    if nei in visited:
                        return False
                    visited.add(nei)
                    q.append((nei, node))

        if len(visited) == n:
            return True
        return False
