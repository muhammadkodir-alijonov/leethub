# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root) -> int:
        result = 0
        
        def dfs(node):
            nonlocal result # Tashqi result o'zgaruvchisini ishlata olish uchun
            
            if not node:
                return 0, 0 # bo'sh node uchun: (sum=0, count=0)
            
            # Chap va o'ng qismlarni hisoblab kelamiz
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            
            # Joriy node uchun umumiy yig'indi va sonini hisoblaymiz
            current_sum = node.val + left_sum + right_sum
            current_count = 1 + left_count + right_count
            
            # Pythonda butun sonli bo'lish uchun // ishlatiladi
            if node.val == current_sum // current_count:
                result += 1
                
            # Tepadagi node uchun javobni qaytaramiz
            return current_sum, current_count

        dfs(root)
        
        return result