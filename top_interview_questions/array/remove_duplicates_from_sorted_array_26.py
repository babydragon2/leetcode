from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        for j in range(1, len(nums)):
            if nums[j] != nums[i-1]:
                nums[i] = nums[j]
                i += 1
        print(nums)
        return i



s = Solution()
nums = [1, 2, 2]
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

print(s.removeDuplicates(nums=nums))
print(s.removeDuplicates(nums=nums2))


