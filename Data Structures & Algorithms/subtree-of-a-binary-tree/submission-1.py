# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == q == None:
            return True
        elif p == None or q==None:
            return False
        elif p.val != q.val:
            return False

        leftIsSame = self.isSameTree(p.left, q.left)
        rightIsSame = self.isSameTree(p.right, q.right)

        return leftIsSame and rightIsSame and (p.val == q.val)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root:
            return False

        check = self.isSameTree(root, subRoot)

        return check or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)