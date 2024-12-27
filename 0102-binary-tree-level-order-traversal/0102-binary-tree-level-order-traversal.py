# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        seen = set()
        queue = [root]
        result = []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node:
                    if node not in seen:
                        seen.add(node)
                        level.append(node.val)
                        queue.append(node.left)
                        queue.append(node.right)
            if level:
                result.append(level)
        return result