# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def analyze(self, root, targetSum, valueSoFar):
        new_sum = valueSoFar + root.val
        if root.left == None and root.right == None:
            return new_sum == targetSum
        else:
            if root.left is not None:
                if self.analyze(root.left, targetSum, new_sum) == True:
                    return True
            if root.right is not None:
                if self.analyze(root.right, targetSum, new_sum) == True:
                    return True
            return False
                
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        else:
            return self.analyze(root,targetSum,0)

        