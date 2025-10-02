from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        taila = None
        na = 0
        p2 = headB
        tailb = None
        nb = 0

        while p1:
            na += 1
            taila = p1
            p1 = p1.next

        while p2:
            nb += 1
            tailb = p2
            p2 = p2.next

        if taila != tailb:
            return None # does not intersect
        
        # another pass with diff adjusted
        while na > nb: 
            headA = headA.next
            na -= 1

        while nb > na:
            headB = headB.next
            nb -= 1

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
