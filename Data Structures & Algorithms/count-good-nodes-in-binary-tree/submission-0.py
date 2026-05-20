# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        goodNodes = 0

        def dfs(root, maxVal):

            nonlocal goodNodes

            if not root:
                return
            
            if root.val >= maxVal:
                goodNodes = goodNodes + 1

            dfs(root.left, max(root.val,maxVal))
            dfs(root.right, max(root.val,maxVal))

        dfs(root, -1000)
        return goodNodes

            

        