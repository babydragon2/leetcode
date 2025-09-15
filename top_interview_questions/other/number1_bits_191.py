
# works but I want to find constant space sol
class Solution1:
    def hammingWeight(self, n: int) -> int:

        b = str(bin(n))
        ans = 0

        for c in b:
            if c == "1":
                ans += 1

        return ans
        

class Solution2:
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()

class Solution3:
    def hammingWeight(self, n: int) -> int:
        ans = 0

        while n:
            ans += n & 1
            n >>= 1

        return ans

class Solution:
    def hammingWeight(self, n: int) -> int:
        # brian kernighan's algorithm
        # by subtracting 1 and &'ing it with the original - we get the next 1 bit
        # if you subtract one it flips all bits to the right of the next 1 bit & removes them
        ans = 0
        while n:
            n &= n-1
            ans += 1
        return ans

