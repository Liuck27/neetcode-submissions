# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # 1- last node of prev (iniziliazzio a Nodo vuoto)
        def invert(node: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            while node.next:
                temp = node.next
                node.next = prev
                prev = node
                node = temp
            node.next = prev
            return node

        
        last_of_prev = ListNode(0)
        start = last_of_prev
        node = head
        
        while node:
            seq_start = node

            for _ in range(k-1):
                if not node.next:
                    return start.next
                node = node.next
            # Punta all'inizio della prossima sequenza
            next_train = node.next
            node.next = None

            # Possiamo invertire (devo ripartire dall'inizio della sequenza)
            node = invert(seq_start)
            last_of_prev.next = node

            # Torniamo alla fine della curr sequence
            for _ in range(k-1):
                node = node.next

            # Ho invertito e ora riattacco quello che segue + mi salvo che è la coda
            node.next = next_train
            last_of_prev = node

            # Iniziamo la nuova seq
            node = node.next

        return start.next
        