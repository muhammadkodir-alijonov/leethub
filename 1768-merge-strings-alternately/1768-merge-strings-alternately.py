# req: 1 <= word1.length, word2.length <= 100
# word1 and word2 consist of lowercase English letters.


class Solution:
    def mergeAlternately(self,word1: str, word2: str) -> str:
        word1_l = len(word1)
        word2_l = len(word2)
        n = min(word1_l, word2_l)
        ans = ''
        for i in range(n):
            ans += word1[i]
            ans += word2[i]
        ans += word1[n:]
        ans += word2[n:]
        return ans

if __name__ == '__main__':
    s = Solution()
    res = s.mergeAlternately('abcd','pq')
    print('res: ' + res)