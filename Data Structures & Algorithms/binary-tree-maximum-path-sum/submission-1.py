# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxpath = -float("inf")
        def path(node):
            if not node:
                return  0
            if not node.left and not node.right:
                self.maxpath = max(self.maxpath, node.val)
                return node.val
            left = max(path(node.left), 0)
            right = max(path(node.right), 0)
            self.maxpath = max(self.maxpath, left + right + node.val)
            return node.val + max(left, right)
        path(root)
        return self.maxpath