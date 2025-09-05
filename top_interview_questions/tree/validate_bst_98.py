from typing import Optional
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # check the bounds for each node (start with the constraints in the problem description)
        # If the node meets the requirements, continue with children passing the updated bounds
        def checknode(t, lb, rb):
            if t:
                if t.val > lb and t.val < rb: # node is valid within the current range, continue with subtrees
                    # for left subtree pass the current value as the upper bound (it can't be more than our current node)
                    # for right subtree pass the current value as the lower bound (it can't be less than our current node)
                    return checknode(t.left, lb, t.val) and checknode(t.right, t.val, rb)
                else:
                    # it is not a valid node in the range - return false
                    return False
            else:
                # leaf node base case - it is valid so return True
                return True
        # use -1 of lower bound, and +1 of upper bound constraint to start
        return checknode(root, -2**31-1, 2**31)


