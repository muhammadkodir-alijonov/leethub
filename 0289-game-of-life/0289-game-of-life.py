# 2 tadan kam 0 qo'shnisi bo'lsa chopamiz
# 2 va 3 ta trik hujayra bo'lsa yani 1 bo'lsa next qilamiz
# 3 tadan ko'p 0 qo'shniis bo'lsa chopamiz
# 3 ta ga teng bo'lgan 0 li hujayra bo'lsa uni trik qilamiz

from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        rows = len(board)
        cols = len(board[0])

        # Yo'nalishlar: 8 ta qo'shni
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        # Deep copy yaratamiz, o'zgartirishlarni bir vaqtda qilamiz
        copy_board = [row[:] for row in board]

        for r in range(rows):
            for c in range(cols):
                live_neighbors = 0
                # 8 tomondan qo'shnilar sonini sanaymiz
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and copy_board[nr][nc] == 1:
                        live_neighbors += 1

                # Current cell rules
                if copy_board[r][c] == 1:
                    # Kam qo'shni yoki ko'p qo'shni — o'ladi
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[r][c] = 0
                else:
                    # O'lik hujayra, aynan 3 qo'shnisi bo'lsa tiriladi
                    if live_neighbors == 3:
                        board[r][c] = 1