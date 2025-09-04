# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # this is the small brain approach
        p = node.next

        while p.next:
            node.val = p.val
            node = p 
            p = p.next

        node.val = p.val
        node.next = None

 
class Solution:
    def deleteNode(self, node):
        # this is the big brain approach
        # just copy the next val and then skip over it (dont forget to cleanup memory if no collector)
        node.val = node.next.val
        node.next = node.next.next

       
