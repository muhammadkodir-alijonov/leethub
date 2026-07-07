from typing import List
from collections import Counter

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        curr = Counter(nums)
        res = []
        for k, v in curr.items():
            print(f"The key is '{k}' and the value is '{v}'")
            if v == 2:
                res.append(k)
        return res