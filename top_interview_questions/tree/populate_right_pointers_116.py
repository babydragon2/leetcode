from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# Don't forget the information we gather in the problem (use the parent's next pointer to set the childs right pointer)
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root and root.left and root.right:
            root.left.next = root.right
            root.right.next = root.next.left if root.next else None

            self.connect(root.left)
            self.connect(root.right)
            return root
