"""
1. Find all permutation and sort them in lexicographical order.
2. we run through right to left
3. and swap it if j<= i
"""
# python
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Modify nums in-place to the next lexicographical permutation.
        """
        n = len(nums)
        if n < 2:
            return

        # find pivot
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # if pivot found, find successor and swap
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # reverse the suffix
        nums[i+1:] = nums[i+1:][::-1]