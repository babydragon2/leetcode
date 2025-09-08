from typing import Optional, List

# Definition for a binary tree node.
# note - for some reason, redefining the treenode class breaks leetcode?

from typing import Optional, List


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(nu):
            n = len(nu)
            if n == 1:
                return TreeNode(val=nu[0])
            elif n == 2:
                tn = TreeNode(val=nu[0])
                tn.right = TreeNode(val=nu[1])
                return tn
            else:
                m = n//2
                tn = TreeNode(val=nu[m])
                tn.left = helper(nu[:m])
                tn.right = helper(nu[m+1:])
                return tn
        root = helper(nums)
        return root

