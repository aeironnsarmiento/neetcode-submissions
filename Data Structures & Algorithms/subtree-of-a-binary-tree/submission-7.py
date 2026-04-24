# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(p, q):
            if not p and not q:
                return True
            
            equal = False

            if p and q and p.val == q.val:
                left = isSame(p.left, q.left)
                right = isSame(p.right, q.right)
                equal = left and right
            else:
                return False

            return equal

        if not root:
            return False
        if not subRoot:
            return True
        if isSame(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)