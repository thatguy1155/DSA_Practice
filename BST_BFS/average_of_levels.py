# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        
        queue = deque([[root,0]])
        result = []
        level_dict = {}
        while queue:
            entry = queue.popleft()
            node = entry[0]
            level = entry[1]

            if level not in level_dict:
                level_dict[level] = [node.val]
            else:
                level_dict[level].append(node.val)

            if node.left:
                queue.append([node.left,(level + 1)])
            if node.right:
                queue.append([node.right,(level + 1)])
        for key in level_dict:
            result.append(sum(level_dict[key])/ len(level_dict[key]))

        return result