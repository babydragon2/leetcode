from typing import Optional

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # reverse the subtree then compare the values inorder 
        def inorder(t1, t2):
            if t1 and t2:
                if t1.val == t2.val:
                    # nodes are the same - reverse subtree of left side and traverse
                    t1.left, t1.right = t1.right, t1.left
                    return inorder(t1.left, t2.left) and inorder(t1.right, t2.right)
                else:
                    # values are unequal - return false
                    return False
            elif not t1 and not t2:
                # both leaf - return true 
                return True
            else:
                return False
        if root:
            return inorder(root.left, root.right)
        else:
            return True

class Solution2:
    # iterative method

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        s1 = [root.left]
        s2 = [root.right]

        while s1 and s2:
            n1 = s1.pop(0)
            n2 = s2.pop(0)
            if n1 and n2:
                if n1.val != n2.val:
                    return False
                else: 
                    n1.left, n1.right = n1.right, n1.left
                    s1.append(n1.left)
                    s1.append(n1.right)
                    s2.append(n2.left)
                    s2.append(n2.right)
            elif not n1 and not n2:
                continue
            else:
                return False
        
        return len(s1) == len(s2)

