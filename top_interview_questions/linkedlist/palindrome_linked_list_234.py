# Definition for singly-linked list.
import re
from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution1:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        i = 0
        j = len(l)-1

        while i < j:
            if l[i] != l[j]:
                return False
            i += 1
            j -= 1
        return True
        
# real solution is to reverse the 2nd half of the list but I CBA 
# to find the center, just use slow/fast method, reverse from where the slow pointer is
# then compare head with prev of the reveral 
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find mindpoint
        slow = head
        fast = head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse 2nd half
        prev = None
        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next

        # compare 
        p1 = head
        p2 = prev

        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True

 
