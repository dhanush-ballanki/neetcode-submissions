# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        res = []
        dr = 0
        q = deque([root] if root else [])
        while q:
            level = deque([])
            for _ in range(len(q)):
                node = q.popleft()
                if dr == 0:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(list(level))
            dr = (dr+1)%2
        return res