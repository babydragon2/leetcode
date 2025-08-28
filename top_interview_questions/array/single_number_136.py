from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        r = 0
        for x in nums:
            r ^= x
        return int(r)

s = Solution()

print(s.singleNumber([4,1,2,1,2]))
print(s.singleNumber([2,2,1]))
print(s.singleNumber([1]))
        
