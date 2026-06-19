class LRUCache:
    class Node:
        def __init__(self, key, val, prev=None, next=None):
            self.val = val
            self.key = key
            self.prev = prev
            self.next = next

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}

        # Initialize your sentinel boundaries
        self.head = self.Node(0, 0)
        self.tail = self.Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self._remove(node)
            self._insert(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # Remove node from list
        if key in self.hashmap:
            self._remove(self.hashmap[key])
        # Put node at the beginning
        new_node = self.Node(key, value)
        self.hashmap[key] = new_node
        self._insert(new_node)
        # Check if size limit exceeded
        if len(self.hashmap) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.hashmap[lru.key]

    def _remove(self, node: Node) -> None:
        # Get the neighbors
        previous_node = node.prev
        next_node = node.next

        # Wire them to each other, bypassing 'node' completely
        previous_node.next = next_node
        next_node.prev = previous_node

    def _insert(self, node: Node) -> None:
        # Track the current first real node in the list
        old_first = self.head.next

        # Connect our new node to its future neighbors
        node.prev = self.head
        node.next = old_first

        # Rewire the head and the old first node to point to our new node
        self.head.next = node
        old_first.prev = node
