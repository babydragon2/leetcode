from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        cur = res

        carry = 0
        while l1 and l2:
            cur.next = ListNode()
            cur = cur.next

            sum = l1.val + l2.val + carry
            cur_sum = (sum) % 10 
            cur.val = cur_sum

            carry = sum // 10

            l1 = l1.next
            l2 = l2.next

        while l1:
            cur.next = ListNode()
            cur = cur.next
            sum = (l1.val + carry)
            cur.val = sum % 10
            carry = sum // 10
            l1 = l1.next

        while l2:
            cur.next = ListNode()
            cur = cur.next
            sum = (l2.val + carry)
            cur.val = sum % 10
            carry = sum // 10 
            l2 = l2.next

        if carry:
            cur.next = ListNode(1)

        return res.next

