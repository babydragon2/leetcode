from typing import List
from functools import cache

# recursive solution with memoization
# O(n) time and space since we store the solution of max subarray for every i->n
# we don't recompute any of the same i's, but we do store them 
class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        @cache
        def helper(i, must_pick):
            # if we have no more elements - return 0 (we won't pick anymore)
            # or if we haven't picked anything - return an absolute min (error condition)
            if i >= len(nums):
                if must_pick:
                    return 0
                else:
                    return -10**5
            else:
                # we can either choose the element or not choose it
                # if we pick it, we must choose the following elements (or return 0 to stop)
                # if we don't pick it - we can start from the next element
                if must_pick:
                    return max(nums[i] + helper(i+1, True), 0)
                else:
                    return max(nums[i] + helper(i+1, True), helper(i+1, False))
        return helper(0, False)

# iterative dp solution we introduce dimensionality for every choice (if we pick or not)
class Solution2:
    def maxSubArray(self, nums: List[int]) -> int: 
        dp = [[0]*len(nums) for _ in range(2)]
        # base cases - for the first ele, the max if we choose will be nums[0] 
        dp[0][0] = nums[0]
        dp[1][0] = nums[0]

        for i in range(1, len(nums)):
            # dp[0][n] - max subarray up to i
            # dp[1][n] - max subarray ending at i
            dp[1][i] = max(dp[1][i-1] + nums[i], nums[i])
            # a bit confusing since dp[0] keeps track of the max at i
            # it is simpler and more effective to just track the max of dp[1] while we iterate
            dp[0][i] = max(dp[0][i-1], dp[1][i])

        return dp[0][-1]

# iterative dp solution we introduce dimensionality for every choice (if we pick or not)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int: 
        dp = [0]*len(nums)
        # base cases - for the first ele, the max if we choose will be nums[0] 
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])

        return max(dp) 

