from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def check(x):
            return sum((num - 1) // x for num in nums) <= maxOperations

        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left