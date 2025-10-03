from typing import Optional, List

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = []

        def inorder(t):
            if t:
                inorder(t.left)
                l.append(t.val)
                inorder(t.right)
            
        inorder(root)
        return l

