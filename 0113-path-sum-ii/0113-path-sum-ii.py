from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        if not root:
            return []
        if not root.left and not root.right:
            if targetSum == root.val:
                return [[root.val]]
            else:
                return []
        stack = [(root, root.val, [])]
        while stack:
            node, total, curr = stack.pop()
            curr.append(node.val)
            if not node.left and not node.right and total == targetSum:
                ans.append(curr)
            if node.left:
                stack.append((node.left, total + node.left.val, curr.copy()))
            if node.right:
                stack.append((node.right, total + node.right.val, curr.copy()))
        return ans