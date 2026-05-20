# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        
        queue = collections.deque()
        queue.append(root)
        result = []

        while queue:
            level_size = len(queue)
            rightnode = None

            for _ in range(level_size):
                node = queue.popleft()
                rightnode = node
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(rightnode.val)

        return result