# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = {}
        final_levels = []
        if root is None:
            return []
        queue = deque([[root,0]])
        while len(queue) > 0:
            item = queue.popleft()
            if item[1] in levels:
                levels[item[1]].append(item[0].val)
            else:
                levels[item[1]] = [item[0].val]
            if item[0].left is not None:
                queue.append([item[0].left,item[1] + 1])
            if item[0].right is not None:
                queue.append([item[0].right,item[1] + 1])
        for i in levels.values():
            final_levels.append(i)
        return final_levels