from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        res = []

        for x in nums1:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1

        for x in nums2:
            if x in d and d[x] > 0:
                res.append(x)
                d[x] -= 1
        return res


s = Solution()

print(s.intersect([1,2,2,1], [2,2]))
print(s.intersect([4,9,5], [9,4,9,8,4]))





