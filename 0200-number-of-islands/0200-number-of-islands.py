from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0
        island_count = 0
        visited = set()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i, j) not in visited:
                    island_count += 1
                    queue = deque([(i, j)])
                    visited.add((i, j))
                    grid[i][j] = '0'

                    while queue:
                        x, y = queue.popleft()

                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < rows and 0 <= ny < cols:
                                if grid[nx][ny] == '1' and (nx, ny) not in visited:
                                    visited.add((nx, ny))
                                    queue.append((nx, ny))
                                    grid[nx][ny] = '0'

        return island_count