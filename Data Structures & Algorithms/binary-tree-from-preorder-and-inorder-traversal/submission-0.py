# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        N = len(preorder)

        def buildTree(pre_start, pre_end, in_start, in_end):

            if (pre_end < pre_start or pre_start < 0 or in_end < in_start or in_start < 0 or pre_end > N or in_end > N ):
                return

            value = preorder[pre_start]
            index = inorder.index(value)
            root = TreeNode(value)

            l_in_start = in_start
            l_in_end = index - 1
            l_pre_start = pre_start + 1
            l_pre_end = l_pre_start + l_in_end - l_in_start

            root.left = buildTree(l_pre_start, l_pre_end, l_in_start, l_in_end)

            r_in_start = index + 1
            r_in_end = in_end
            r_pre_start = l_pre_end + 1
            r_pre_end = r_pre_start + r_in_end - r_in_start

            root.right = buildTree(r_pre_start, r_pre_end, r_in_start, r_in_end)

            return root

        return buildTree(0, N-1, 0, N-1)
