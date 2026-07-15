class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
    
        # Har bir katakka kelish uchun minimal summalarni saqlaymiz
        # Boshida barchasini cheksiz (float('inf')) qilamiz
        min_sum = [[float('inf')] * n for _ in range(m)]
        min_sum[0][0] = grid[0][0]
        
        # Heap (Navbat): (summa, satr, ustun)
        queue = [(grid[0][0], 0, 0)]
        
        while queue:
            current_sum, r, c = heapq.heappop(queue)
            
            # Agar oxirgi katakka yetib kelsak, bu eng minimal yo'l bo'ladi
            if r == m - 1 and c == n - 1:
                return current_sum
                
            # Agar joriy summa avval topilgan minimal summadan katta bo'lsa, o'tkazib yuboramiz
            if current_sum > min_sum[r][c]:
                continue
                
            # Faqat pastga (down) va o'ngga (right) yurish mumkin
            for dr, dc in [(1, 0), (0, 1)]:
                nr, nc = r + dr, c + dc
                
                # Grid chegarasidan chiqib ketmaslikni tekshiramiz
                if 0 <= nr < m and 0 <= nc < n:
                    new_sum = current_sum + grid[nr][nc]
                    
                    # Agar yangi topilgan yo'l yaxshiroq (kichikroq) bo'lsa
                    if new_sum < min_sum[nr][nc]:
                        min_sum[nr][nc] = new_sum
                        heapq.heappush(queue, (new_sum, nr, nc))
                        
        return min_sum[m-1][n-1]