from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []
        queue = deque([root])
        flag = True

        while queue:
            curr = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    curr.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

            if not flag:
                curr.reverse()

            ans.append(curr)
            flag = not flag

        return ans
