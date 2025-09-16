from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # xor the range [0, n] then xor nums, the missing element will be left
        # any number x ^ x = 0, so duplicates will cancel each other out
        # xor is also communitive so it works on nums which is out of order
        r = 0
        for i in range(1, len(nums)+1):
            r ^= i
        for x in nums:
            r ^= x
        return r

        
