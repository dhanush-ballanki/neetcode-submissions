# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.postOrder(root, res)
        return res

    def postOrder(self, node, res):
        if not node:
            return None
        self.postOrder(node.left, res)
        self.postOrder(node.right, res)
        res.append(node.val)