class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lnums = len(nums)
        count = 0
        for i in range(lnums):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        return count