class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        temp_node = None
        if root is None:
            return root
        if root.left is None and root.right is None:
            return root
        if root.left:
            if root.right:
                root.right = self.invertTree(root.right)
                temp_node = root.right
            root.left = self.invertTree(root.left)
            root.right = root.left
            if temp_node is not None:
                root.left = temp_node
            else:
                root.left = None
        elif root.right:
            root.right = self.invertTree(root.right)
            root.left = root.right
            root.right = None
        return root
    
class LessSpaceSolution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(node):
            if not node:
                return None
            if not node.left and not node.right:
                return node

            node.left, node.right = node.right, node.left
            invert(node.left)
            invert(node.right)
            return node
        return invert(root)