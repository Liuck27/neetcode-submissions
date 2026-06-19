"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return

        hm = defaultdict(Node)
        hm[None] = None

        start = head
        
        while head:
            newNode = Node(head.val)
            hm[head] = newNode
            head = head.next

        head = start
        while head:
            hm[head].next = hm[head.next]
            hm[head].random = hm[head.random]
            head = head.next

        return hm[start]
