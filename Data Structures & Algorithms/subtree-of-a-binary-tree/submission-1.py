# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 
# given: root (full tree) and subroot (small tree)
# [1,2,3,4,5] and [2,4,5]
# only check once we have the same root and subroot 
# check through full tree:
# 1 false
# 2 == 2 true

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if not p and not q:
                return True
            equal = False
            if p and q and p.val == q.val:
                leftSame = isSameTree(p.left, q.left)
                rightSame = isSameTree(p.right, q.right)
                equal = leftSame and rightSame
            else:
                return False
            return equal

        if not subRoot:
            return True
        if not root:
            return False

        if isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        