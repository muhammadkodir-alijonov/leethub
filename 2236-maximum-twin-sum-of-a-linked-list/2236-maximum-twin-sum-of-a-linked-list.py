# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next

        max_sum = 0
        for i in range(length // 2):
            twin_sum = values[i] + values[length - 1 - i]
            max_sum = max(max_sum, twin_sum)

        return max_sum
