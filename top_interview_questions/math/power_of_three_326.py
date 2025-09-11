from math import log

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        y = log(n,3)
        y = round(y, 10) 
        return 3**y == n

s = Solution()
print(s.isPowerOfThree(243))
