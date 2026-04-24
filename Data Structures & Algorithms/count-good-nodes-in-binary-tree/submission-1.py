# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = [0]
        def dfs(root, maxNum):
            if not root:
                return 0
            maxNum = max(maxNum, root.val)
            left, right = dfs(root.left, maxNum), dfs(root.right, maxNum)
            if root.val >= maxNum:
                count[0] += 1
        dfs(root, root.val)
        return count[0]