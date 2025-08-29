from typing import List

class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        res = [-1, -1]

        for i in range(len(nums)):
            d[nums[i]] = i
        
        for i in range(len(nums)):
            y = target - nums[i] 
            if y in d and d[y] != i:
                res = [i,d[y]]
                break
        return res

# this solution returns immediately optimizing performance - beats 100% compared to 44%
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        res = [-1, -1]

        for i in range(len(nums)):
            d[nums[i]] = i
            y = target - nums[i] 
            if y in d and d[y] != i:
                return [i,d[y]]
             
        
        for i in range(len(nums)):
            y = target - nums[i] 
            if y in d and d[y] != i:
                res = [i,d[y]]
                break
        return res


s = Solution()
print(s.twoSum([2,7,11,15],9))
print(s.twoSum([3,2,4],6))


