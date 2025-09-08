from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        r = m+n-1
        l = m-1
        k = n-1
        
        while k >= 0:
            if l >= 0 and nums1[l] > nums2[k]:
                nums1[r] = nums1[l]
                l -= 1
            else:
                nums1[r] = nums2[k]
                k -= 1
            r -= 1



s = Solution()
s.merge([1,2,3,0,0,0], 3, [2, 5, 6], 3)

        
