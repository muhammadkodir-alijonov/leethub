from typing import List
from collections import defaultdict

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        # Har bir qator va ustun uchun min va max koordinatalarni saqlash
        row_min = defaultdict(lambda: float('inf'))
        row_max = defaultdict(lambda: float('-inf'))
        col_min = defaultdict(lambda: float('inf'))
        col_max = defaultdict(lambda: float('-inf'))

        # 1-qadam: Barcha binolarni bir marta ko'rib chiqib, chegaralarni aniqlash
        for x, y in buildings:
            if y < row_min[x]: row_min[x] = y
            if y > row_max[x]: row_max[x] = y
            if x < col_min[y]: col_min[y] = x
            if x > col_max[y]: col_max[y] = x

        covered = 0
        # 2-qadam: Har bir bino uchun tekshirish (O(1) operatsiya)
        for x, y in buildings:
            # Chapda bino bormi? (shu qatordagi eng kichik y bizdan kichikmi)
            has_left = row_min[x] < y
            # O'ngda bino bormi? (shu qatordagi eng katta y bizdan kattami)
            has_right = row_max[x] > y
            # Yuqorida bino bormi? (shu ustundagi eng kichik x bizdan kichikmi)
            has_up = col_min[y] < x
            # Pastda bino bormi? (shu ustundagi eng katta x bizdan kattami)
            has_down = col_max[y] > x

            if has_left and has_right and has_up and has_down:
                covered += 1
                
        return covered