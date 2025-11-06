from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start=0):
            if start == len(nums):
                result.append(nums[:])
                return

            seen = set()  
            for i in range(start, len(nums)):
                if nums[i] in seen:
                    continue
                seen.add(nums[i])

                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack()
        return result