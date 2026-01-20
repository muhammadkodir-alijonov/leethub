# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of English uppercase letters.
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        s = len(str1)
        t = len(str2)
        if t > s:
            str1, str2 = str2, str1
        if str1[:len(str2)] == str2:
            if str1 == str2:
                return str1
            return self.gcdOfStrings(str1[len(str2):], str2)
        return ''