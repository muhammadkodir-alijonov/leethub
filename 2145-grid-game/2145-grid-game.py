from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        prefix1 = [0] * (n + 1)
        prefix2 = [0] * (n + 1)

        for j in range(n):
            prefix1[j + 1] = prefix1[j] + grid[0][j]
            prefix2[j + 1] = prefix2[j] + grid[1][j]

        min_score = float('inf')
        for j in range(n):

            top = prefix1[n] - prefix1[j + 1]
            bottom = prefix2[j]
            player2_score = max(top, bottom)

            min_score = min(min_score, player2_score)

        return min_score
