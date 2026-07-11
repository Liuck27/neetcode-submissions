# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root: 
            return ""

        tree = []
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node:
                tree.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                tree.append(None)
        
        out = "#".join(map(str,tree))
        return out


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
            
        tokens = data.split("#")
        
        # 1. Create the true root
        root = TreeNode(int(tokens[0]))
        q = deque([root])
        
        # 2. Use a pointer to scan through the tokens
        i = 1
        
        while q and i < len(tokens):
            curr = q.popleft()
            
            # Process Left Child
            if tokens[i] != "None":
                curr.left = TreeNode(int(tokens[i]))
                q.append(curr.left)
            i += 1
            
            # Process Right Child (Make sure we don't go out of bounds)
            if i < len(tokens) and tokens[i] != "None":
                curr.right = TreeNode(int(tokens[i]))
                q.append(curr.right)
            i += 1
            
        return root














