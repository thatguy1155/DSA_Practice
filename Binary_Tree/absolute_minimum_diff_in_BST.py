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

#crappy attempt
def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_left = 9999999999999
        min_right = 9999999999999
        if root.left == None and root.right == None:
            return None
        if root.left:
            curr_diff_left = abs(root.val - root.left.val)
            min_so_far_left = self.getMinimumDifference(root.left)
            if min_so_far_left is not None:
                min_left = min(curr_diff_left,min_so_far_left)
            else:
                min_left = curr_diff_left
        if root.right:
            curr_diff_right = abs(root.val - root.right.val)
            min_so_far_right = self.getMinimumDifference(root.right)
            if min_so_far_right is not None:
                min_right = min(curr_diff_right,min_so_far_right)
            else:
                min_right = curr_diff_right
        return min(min_left,min_right)