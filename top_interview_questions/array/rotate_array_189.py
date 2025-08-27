from typing import List


# Works but gets TLE
class Solution3:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        k = len(nums) - k

        for i in range(k):
            # perform a single rotation k times 
            for j in range(1, len(nums)):
                nums[j], nums[j-1] = nums[j-1], nums[j]

class Solution1:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        d = n-k
        nums = (nums[d:] + nums[:d])
        print(nums)


# Real solution: roate the array 3 times, the entire array, the first k, then the rest
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        nums.reverse()

        k = k % len(nums)

        l = 0
        r = k-1 

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        l = k 
        r = len(nums)-1 
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1


s = Solution()
s.rotate([1,2,3,4,5,6,7], 3)


