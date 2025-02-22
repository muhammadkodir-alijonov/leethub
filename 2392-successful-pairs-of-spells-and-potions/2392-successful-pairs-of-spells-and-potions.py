from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()  # Sort potions for binary search
        result = []

        for spell in spells:
            left, right = 0, len(potions)  
            while left < right:
                mid = (left + right) // 2
                if spell * potions[mid] >= success:
                    right = mid  
                else:
                    left = mid + 1 
            
            result.append(len(potions) - left) 
        
        return result