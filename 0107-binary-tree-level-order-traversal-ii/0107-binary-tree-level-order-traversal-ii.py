# Definition for a binary tree node.
from typing import Optional,List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        seen =set()
        queue = deque([root])
        ans = []
        while queue:
            curr = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    if node not in seen:
                        seen.add(node)
                        curr.append(node.val)
                        queue.append(node.left)
                        queue.append(node.right)
            if curr:
                ans.append(curr)
        ans.reverse()
        return ans
    