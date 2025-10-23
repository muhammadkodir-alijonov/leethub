# Definition for singly-linked list.

# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]

# We must solve the problem in O(1) extra space complexity and O(n) time complexity.
# separate list first odd and then even indexes' number

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd = head
        even = head.next
        even_head = even
        while even and even.next:
            odd.next = odd.next.next
            print(odd.val)
            even.next = even.next.next
            print(even.val)
            odd = odd.next
            even = even.next
        odd.next = even_head
        return head