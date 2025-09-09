# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        # do binary search in range n - make calls to api to check if bad version
        l = 1
        r = n 
        lbv = -1

        while l <= r:
            m = (l+r)//2

            if isBadVersion(m):
                lbv = m
                # bs the lower half
                r = m-1
            else:
                # bs the upper half
                l = m+1

        return lbv
        

