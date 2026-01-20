class Solution:
    def mergeAlternately(self,word1: str, word2: str) -> str:
        result = ""
        for i in range(min(len(word1), len(word2))):
            result += word1[i] + word2[i]
        result += word1[len(word2):] + word2[len(word1):]
        return result