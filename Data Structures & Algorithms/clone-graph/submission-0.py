"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
from collections import defaultdict
from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_to_new = defaultdict(Node)
        old_to_new[node] = Node(node.val)

        queue = deque([node])

        while len(queue)>0:
            n = queue.popleft()

            for neigh in n.neighbors:
                if neigh not in old_to_new:
                    old_to_new[neigh] = Node(neigh.val)
                    queue.append(neigh)

                old_to_new[n].neighbors.append(old_to_new[neigh])
                
        return old_to_new[node]
        