from typing import Optional

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(t):
            if t:
                return max(dfs(t.left), dfs(t.right)) + 1
            else:
                return 0
        return dfs(root)

        
