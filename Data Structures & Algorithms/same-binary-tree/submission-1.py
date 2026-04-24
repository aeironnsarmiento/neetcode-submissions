# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 
# 1, 2, 3 | 1, 2, 3
# 1 and 1
# 2 and 2 (q.left and p.left)
# 3 and 3 (q.right and p.right)

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        equal = False

        if p and q and p.val == q.val:
            equal = self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

        return equal