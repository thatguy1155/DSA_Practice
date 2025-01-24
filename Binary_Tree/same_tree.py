# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        is_same = True
        if p is None and q is not None:
            return False
        if q is None and p is not None:
            return False
        if p is None and q is None:
            return  True
        if p.val != q.val:
            return False
        if (p.left is None and q.left is not None) or (p.left is not None and q.left is None):
            return False
        if (p.right is None and q.right is not None) or (p.right is not None and q.right is None):
            return False
        if p.left and q.left:
            is_same = self.isSameTree(p.left,q.left)
        if p.right and q.right and is_same != False:
            is_same = self.isSameTree(p.right,q.right)
        return is_same
        