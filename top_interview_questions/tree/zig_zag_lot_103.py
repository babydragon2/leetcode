from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        q = deque()

        if not root:
            return []

        q.append(root)
        swap = True # read right to left, if false, reverse it
        while q:
            level = []
            nextlevel = []
            for x in q:
                level.append(x.val)
                if x.right:
                    nextlevel.append(x.right)
                if x.left:
                    nextlevel.append(x.left)

            if swap:
                level.reverse()
                swap = False
            else:
                swap = True
            ans.append(level)
            q = nextlevel
        return ans


        
