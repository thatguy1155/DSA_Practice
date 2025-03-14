class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        #note: it's super crucial when accessing variables from within dfs to turn it into a list
        the_sum = [0]
        def dfs(root):
            the_sum[0] += 1
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            return the_sum
        dfs(root)
        return the_sum[0]