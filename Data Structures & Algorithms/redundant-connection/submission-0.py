class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)
        # If nodes are 1-indexed up to N
        parent = [i for i in range(n + 1)]

        def find(node):
            if parent[node] == node:
                return node
            # Path compression: update pointer to the root parent directly
            parent[node] = find(parent[node]) 
            return parent[node]

        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)
            
            if root1 == root2:
                return False # Cycle detected!
            
            # Merge: Make one root point to the other
            parent[root1] = root2
            return True
        
        for u, v in edges:
            if not union(u, v):
                return [u, v]