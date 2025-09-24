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
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        ABS_MAX = float("inf")
        ABS_MIN = float("-inf")

        lm = [ABS_MAX for _ in nums]
        rm = [ABS_MIN for _ in nums]

        # compute the left mins in the range [0, i-1]
        for i in range(1, len(nums)):
            lm[i] = min(lm[i-1], nums[i])

        # compute the right maxes in range [i+1, n-1]
        for i in reversed(range(len(nums))):


 
s = Solution() 
print(s.increasingTriplet([2,1,5,0,4,6]))
print(s.increasingTriplet([5,4,3,2,1]))
print(s.increasingTriplet([1,2,3,4,5]))

