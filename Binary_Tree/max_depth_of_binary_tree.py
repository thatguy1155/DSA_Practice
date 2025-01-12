# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left == None and root.right == None:
            return 1
        else:
            left_sum = 0
            right_sum = 0
            if root.left is not None:
                left_sum = self.maxDepth(root.left)
            if root.right is not None:
                right_sum = self.maxDepth(root.right)
            if left_sum >= right_sum:
                return left_sum + 1
            else:
                return right_sum + 1
        