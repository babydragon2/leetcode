from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        res = head
        h2 = head.next
        while head and head.next and head.next.next:
            prev = head.next
            head.next = head.next.next
            prev.next = prev.next.next
            head = head.next
        head.next = h2
        return res

        
