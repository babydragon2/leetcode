from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# not optimized - O(n) ts
class Solution1:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        l = []

        def inorder(t):
            if t:
                inorder(t.left)
                l.append(t.val)
                inorder(t.right)

        inorder(root)
        return l[k-1]


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # define globals for k and the result
        # if its difficult to return some intermediate value during the recursion
        # just set a flag and a variable
        self.k = k
        self.res = None

        def inorder(t):
            if t:
                inorder(t.left)

                # visit the current node, if k == 0 get solution
                self.k -= 1
                if self.k == 0:
                    self.res = t.val

                inorder(t.right)
        inorder(root)
        return self.res
