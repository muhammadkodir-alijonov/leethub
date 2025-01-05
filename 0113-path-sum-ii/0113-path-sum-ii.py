from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, current_sum, path):
            if not node:
                return
            current_sum += node.val
            path.append(node.val)
            if not node.left and not node.right and current_sum == targetSum:
                ans.append(path[:])
            dfs(node.left, current_sum, path)
            dfs(node.right, current_sum, path)
            path.pop()

        ans = []
        dfs(root, 0, [])
        return ans