from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def levelOrder(self,root):
        if root is None:
            return []

        # Create an empty queue for level order traversal
        q = deque()
        res = []

        # Enqueue Root
        q.append(root)
        currLevel = 0

        while q:
            len_q = len(q)
            res.append([])

            for _ in range(len_q):
                # Add front of queue and remove it from queue
                node = q.popleft()
                res[currLevel].append(node.val)

                if node.left is not None or node.right is not None:
                    # Enqueue left child
                    if node.left is not None:
                        q.append(node.left)
                    else:
                        q.append(TreeNode(-666,None,None))

                    # Enqueue right child
                    if node.right is not None:
                        q.append(node.right)
                    else:
                        q.append(TreeNode(-666,None,None))
                elif node.val != -999:
                    q.append(TreeNode(-999,None,None))
                    q.append(TreeNode(-999,None,None))
                
            currLevel += 1

        return res

    def is_palindrome(self,array):
        l = 0
        r = len(array) - 1

        while r > l:
            if array[r] != array[l]:
                return False
            else:
                l += 1
                r -= 1
        return True
      
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        res = self.levelOrder(root)
        symmetry_flag = True
        for level in res:
            symmetrical = self.is_palindrome(level)
            if symmetrical == False:
                return False
            
        return True

        