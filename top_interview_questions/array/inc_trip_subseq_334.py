from typing import List

# brute force TLE
class Solution1:
    def increasingTriplet(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] < nums[j] < nums[k]:
                        return True

        return False
        
# optimize O(n^2) - fix the middle element and scan to the left and right
class Solution2:
    def increasingTriplet(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            l = i-1
            r = i+1

            # scan left such that nums[l] < nums[i]
            found_left = False
            found_right = False
            while l >= 0:
                if nums[i] > nums[l]:
                    found_left = True
                    break
                l -= 1

            while r < len(nums):
                if nums[r] > nums[i]:
                    found_right = True
                    break
                r += 1
            if found_right and found_left:
                return True

        return False

# Precompute min and max for each range
class Solution3:
    def increasingTriplet(self, nums: List[int]) -> bool:
        ABS_MAX = float("inf")
        ABS_MIN = float("-inf")

        lm = [ABS_MAX for _ in nums]
        rm = [ABS_MIN for _ in nums]
        lm[0] = nums[0]
        rm[len(nums)-1] = nums[len(nums)-1]

        # compute the left mins in the range [0, i-1]
        for i in range(1, len(nums)):
            lm[i] = min(lm[i-1], nums[i])

        # compute the right maxes in range [i+1, n-1]
        for i in reversed(range(len(nums)-1)):
            # print(i, rm[i+1], nums[i])
            rm[i] = max(rm[i+1], nums[i])
        
        # print(nums)
        # print(lm, rm)
        for i in range(1, len(nums)-1):
            if lm[i] < nums[i] < rm[i]:
                return True

        return False

# optimized 2 pass solution - accepted but not optimal
class Solution4:
    def increasingTriplet(self, nums: List[int]) -> bool:
        ABS_MAX = float("inf")
        ABS_MIN = float("-inf")
        n = len(nums)

        lm = [ABS_MAX] * n 
        rm = [ABS_MIN] * n
        lm[0] = nums[0]
        rm[n-1] = nums[n-1]


        l = 1
        r = n-2

        while l < n and r >= 0:
            lm[l] = min(lm[l-1], nums[l])
            rm[r] = max(rm[r+1], nums[r])
            l += 1
            r -= 1
        

        for i in range(1, len(nums)-1):
            if lm[i] < nums[i] < rm[i]:
                return True

        return False

# greedy o(n) one pass O(1) space
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float("inf")
        second = float("inf")

        # greedy, keep track of the last 2 minimums (update them in order)
        # if we reach a third minimum - we are done
        for x in nums:
            if x <= first:
                first = x
            elif x <= second:
                second = x
            else:
                return True
        return False


 
 
s = Solution() 
print(s.increasingTriplet([2,1,5,0,4,6]))
print(s.increasingTriplet([5,4,3,2,1]))
print(s.increasingTriplet([1,2,3,4,5]))

