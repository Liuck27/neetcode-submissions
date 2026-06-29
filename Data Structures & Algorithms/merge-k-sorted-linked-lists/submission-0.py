# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return 

        heap = []
        head =  ListNode()
        res = head
        alive = 0

        for i, node in enumerate(lists):
            if lists[i]:
                heap.append((node.val, i, node))
                alive += 1

        heapq.heapify(heap)

        while alive:
            _, i, node = heapq.heappop(heap)
            res.next = node
            res = res.next
            lists[i] = lists[i].next
            if lists[i]:
                heapq.heappush(heap,(lists[i].val, i, lists[i]))
            else:
                alive -= 1

        res.next = None
            

        return head.next
