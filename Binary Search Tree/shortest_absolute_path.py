# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_distance = [float('inf')]
        prev = [None]

        def dfs(node):
            if node is None:
                return None
            dfs(node.left)

            if prev[0] is not None:
                min_distance[0] = min(min_distance[0],node.val - prev[0]) # we know that because it's in-order traversal that prev value will always be less that current val
            prev[0] = node.val

            dfs(node.right)

        dfs(root)
        return min_distance[0]