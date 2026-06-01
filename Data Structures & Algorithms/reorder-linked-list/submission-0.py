# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            return

        #arriva a metà lista, da lì in poi inverti
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #inverti fa metà in avanti
        curr = slow.next
        slow.next = None
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        first, second = head, prev
        #ora hai 2 liste,ricomponi prendendo un nodo da ciascuna

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
        