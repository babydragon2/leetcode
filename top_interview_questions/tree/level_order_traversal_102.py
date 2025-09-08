from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS but process the entire queue at once (to get the entire level)
        q = [root]
        res = []

        while q:
            new_q = []
            agg = []
            for x in q:
                if x:
                    agg.append(x.val)
                    new_q.append(x.left)
                    new_q.append(x.right)
            if agg != []:
                res.append(agg)
            q = new_q

        return res
        
