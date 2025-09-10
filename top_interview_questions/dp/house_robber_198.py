from typing import List
from functools import cache

class Solution1:
    def rob(self, nums: List[int]) -> int:

        @cache 
        def helper(i):
            if i >= len(nums):
                return 0
            else:
                return max(nums[i] + helper(i+2), helper(i+1))

        return helper(0)

 
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        dp[0] = nums[0]
        if len(nums) < 2:
            return nums[0]

        dp[1] = max(nums[0], nums[1]) 

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return max(dp)
          
