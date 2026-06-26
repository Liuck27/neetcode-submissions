class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        visited = set()
        neigh = defaultdict(set)

        for edge in edges:
            s = edge[0]
            e = edge[1]
            neigh[s].add(e)
            neigh[e].add(s)

        q = deque()
        q.append((0,-1))

        while q:
            node, parent = q.popleft()
            visited.add(node)

            for nei in neigh[node]:
                if nei != parent:
                    if nei in visited:
                        return False
                    q.append((nei,node))


        if len(visited) == n:
            return True
        return False

        