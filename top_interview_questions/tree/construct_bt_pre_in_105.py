from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Simple recursive solution: O(n^2) due to inefficient index lookup
# The for any node in inorder, the elements of the left subtree are to the left, and right to the right
# this means that the root_idx inorder = # of elements in the left subtree
# since preorder goes from left->root->right the count of elements will be the same
# for preorder left -> pass the left subtree [1, root_idx]
# for preorder right -> pass the right subtree [root_idx+1, n)
# for inorder pass the left elements (excluding the root), we must also limit this list
# even though the relative order should tell us - because otherwise the sizes of the next subtrees won't align with the preorder list
# for inoorder pass the right elements (excluding the root) -> [root_idx+1:]
# this solution is very confusing
class Solution1:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root_val = preorder[0]
        root_idx = inorder.index(root_val)
        node = TreeNode(root_val)

        node.left = self.buildTree(preorder[1:root_idx+1], inorder[:root_idx])
        node.right = self.buildTree(preorder[root_idx+1:], inorder[root_idx+1:])

        return node

# optimized approch with indexOf precomute
# we also need to keep track of left and right bounds instead of slicing (this is also more efficient)
# otherwise the indexOf mapping will not translate to the sliced lists (unless we recompute it each time - but then there is no speedup)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        d = {x:i for i,x in enumerate(inorder)}
        root_idx = 0

        # left and right bound the elements in the current subtree
        def helper(left, right):
            nonlocal root_idx
            if left > right:
                # no more nodes to check, we are all out
                return None
            
            root_val = preorder[root_idx]
            root_idx += 1
            node = TreeNode(root_val)

            mid = d[root_val]
            node.left = helper(left, mid-1) 
            node.right = helper(mid+1, right) 
            return node
        
        return helper(0, len(preorder)-1)


