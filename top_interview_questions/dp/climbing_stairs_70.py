class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        stairs = [0]*(n)
        stairs[0] = 1
        stairs[1] = 2

        for i in range(2, n):
            stairs[i] = stairs[i-1] + stairs[i-2]
        
        return stairs[n-1]

# recursive solution to derive recurrence relation - TLE if try to submit
class Solution1:
    def climbStairs(self, n: int) -> int:
        def h(i, total):
            if i == total:
                return 1
            elif i > total:
                return 0
            else:
                return h(i+1, total) + h(i+2, total)
        return h(0, n)

s1 = Solution()
print(s1.climbStairs(2), "ans:", 2)
print(s1.climbStairs(3), "ans:", 3)
        
        
