from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # imagine 0 is -1 and 1 is +1 , count is summ of distacne of 0 and 1
        count = 0 # if the count occured before, 0 and 1 distamce are equal:
        max_len = 0
        dic_ = {0:-1}
        for i  in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            if nums[i] == 1:
                count += 1
            if count in dic_: # is that if count has already occurred before
                max_len = max(max_len, i - dic_[count]) # we calculate the distance from the first occurrence of count to the current index i.
            else:
                dic_[count] = i
        return max_len