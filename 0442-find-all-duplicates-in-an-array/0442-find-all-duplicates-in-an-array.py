# if nums  null return []
# 1. we can use hashmap to calculate how many twise elemetn in list
# 2. Sort and calculate

from typing import List
from collections import Counter

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        curr = dict()
        for i in nums:
            if i in curr:
                curr[i] += 1
            else:
                curr[i] = 1
        res = []
        for k, v in curr.items():
            print(f"The key is '{k}' and the value is '{v}'")
            if v == 2:
                res.append(k)
        return res