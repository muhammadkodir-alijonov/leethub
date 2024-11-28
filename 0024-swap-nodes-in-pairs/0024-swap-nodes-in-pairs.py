# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = head
        curr = head.next if head else None
        while curr:
            pre.val, curr.val = curr.val, pre.val
            pre = curr.next
            if not pre:
                break
            curr = pre.next
        return head