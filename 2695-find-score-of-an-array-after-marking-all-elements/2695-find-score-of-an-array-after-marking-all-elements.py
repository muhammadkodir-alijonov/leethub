from typing import List

class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        visited = [False] * n  
        score = 0

        indexed_nums = sorted((value, idx) for idx, value in enumerate(nums))

        for value, idx in indexed_nums:
            if visited[idx]:
                continue  

            score += value

            visited[idx] = True
            if idx > 0:
                visited[idx - 1] = True
            if idx < n - 1:
                visited[idx + 1] = True

        return score