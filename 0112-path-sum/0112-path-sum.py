# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum == root.val
        seen = [(root, root.val)]
        queue = [(root, root.val)]
        while queue:
            node, total = queue.pop()
            if not node.left and not node.right and total == targetSum:
                return True
            if node.left:
                queue.append((node.left, total + node.left.val))
            if node.right:
                queue.append((node.right, total + node.right.val))
        return False