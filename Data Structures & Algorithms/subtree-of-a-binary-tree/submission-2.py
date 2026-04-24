# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(list1, list2):
            if not list1 and not list2:
                return True

            equal = False

            if list1 and list2 and list1.val == list2.val:
                leftE = isSameTree(list1.left, list2.left)
                rightE = isSameTree(list1.right, list2.right)
                equal = leftE and rightE
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

