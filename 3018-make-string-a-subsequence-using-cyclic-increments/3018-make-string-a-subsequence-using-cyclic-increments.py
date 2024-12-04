class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        left, right = 0, len(str1)
        j = 0  
        while left < right and j < len(str2):  
            if str1[left] == str2[j]:  
                j += 1  
            elif (ord(str1[left]) - ord('a') + 1) % 26 + ord('a') == ord(str2[j]): 
                j += 1  
            left += 1  
        return j == len(str2)