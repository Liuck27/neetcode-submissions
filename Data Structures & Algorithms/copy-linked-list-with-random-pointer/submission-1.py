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

        start = head
        newNode = Node(head.val, None)

        while head:
            
            newNext = Node(0, None)
            newNode.val = head.val
            
            hm[head] = newNode

            head = head.next
            if head:
                newNode.next = newNext
                newNode = newNode.next

        head = start
        while head:
            if head.random:
                hm[head].random = hm[head.random]
            head = head.next

        return hm[start]
