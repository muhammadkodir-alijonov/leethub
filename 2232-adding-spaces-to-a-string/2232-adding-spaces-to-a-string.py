from typing import List

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        space_index = 0
        for i in range(len(s)):
            if space_index < len(spaces) and i == spaces[space_index]:
                ans.append(" ")
                space_index += 1
            ans.append(s[i])
        return "".join(ans)