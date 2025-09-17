from typing import List
from collections import defaultdict

# gets TLE - probably due to trying to insert too many duplicates
class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # dump all nums in a dict
        # iterate over all pair sums and check complement in dict
        res = [] 

        d = defaultdict(list)

        for i in range(len(nums)):
            d[nums[i]].append(i)

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                c = sum * -1
                if d[c]:
                    idxs = d[c]
                    for x in idxs:
                        if x != i and x != j:
                            triplet = sorted([nums[i], nums[j], nums[x]])
                            if triplet not in res:
                                res.append(triplet)
        return res 

# still TLE - not true O(n^2) since dict buckets can be O(n^2) in the case where nums is all 0's
# if we want to avoid duplicates efficently, we need to build triplets in a traversal order
# so instead need to go with a sorted approach
class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # do it the other way around - get all complements then check one by one
        res = set() 
        d = defaultdict(list)

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                c = -1 * sum
                d[c].append((i, j))


        for i in range(len(nums)):
            for pair in d[nums[i]]:
                if i not in pair:
                    j, k = pair
                    triplet = tuple(sorted((nums[i], nums[j], nums[k])))
                    res.add(triplet)

        return list(res) 

# two pointer approach is O(n^2) - I miscalculated and thought it was O(n^3) but due to the sort the innerloop is O(n)
# easy case - just use a set, otherwise make sure we iterate over all duplicates at each step 
class Solution3:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # use three pointers after sorting
        res = []
        nums.sort()

        i = 0 
        for i in range(len(nums)):
            # check previous i (as long as we are not at 0) to see if its the same
            # if it is, continue as we have already calculated for this value (gets rid of duplicates)
            # or we can use a set
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1 
            k = len(nums) - 1
            while j < k:
                # also have to skip duplicates of j and k, or use a set
                sum = nums[i] + nums[j] + nums[k] 
                if sum == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    
                    while j < k and nums[j] == nums[j-1]:
                        j += 1

                    while j < k and nums[k] == nums[k+1]:
                        k -= 1

                elif sum < 0:
                    j += 1
                else:
                    k -= 1
        return res

# there is another approach which uses negative, postive and 0 sets, but this is not intuitive
# it basically removes the duplicates without losing information (you keep a 0 count and compare all combinations of positive and negative numbers)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = set()

        #1. Split nums into three lists: negative numbers, positive numbers, and zeros
        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0: 
                n.append(num)
            else:
                z.append(num)

        #2. Create a separate set for negatives and positives for O(1) look-up times
        N, P = set(n), set(p)

        #3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
        #   i.e. (-3, 0, 3) = 0
        if z:
            for num in P:
                if -1*num in N:
                    res.add((-1*num, 0, num))

        #3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
        if len(z) >= 3:
            res.add((0,0,0))

        #4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
        #   exists in the positive number set
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                target = -1*(n[i]+n[j])
                if target in P:
                    res.add(tuple(sorted([n[i],n[j],target])))

        #5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
        #   exists in the negative number set
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                target = -1*(p[i]+p[j])
                if target in N:
                    res.add(tuple(sorted([p[i],p[j],target])))

        return list(res)
    

s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))
print(s.threeSum([0, 0, 0]))
print(s.threeSum([0, 1 ,1]))

