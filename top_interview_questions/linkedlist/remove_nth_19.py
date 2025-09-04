from typing import Optional

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = ListNode(0, head)
        dummy = res

        # we know n <= size
        for _ in range(n):
            if head:
                head = head.next

        while head and dummy:
            head = head.next
            dummy = dummy.next

        # we land before the node to remove
        if dummy and dummy.next:
            dummy.next = dummy.next.next

        return res.next 


            
