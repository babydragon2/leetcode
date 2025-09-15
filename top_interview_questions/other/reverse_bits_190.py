class Solution1:
    def reverseBits(self, n: int) -> int:
        # cring sol
        s = str(bin(n))[2:]
        if len(s) < 32:
            # add missing 0's for 32 bit integer
            diff = 32 - len(s)
            s = "0"*diff + s
        s2 = [x for x in reversed(s)]
        # print(s, s2)
        ans = 0
        i = len(s2)-1
        p = 0
        while i >= 0:
            if s2[i] == "1":
                ans += 2 ** p
            i -= 1
            p += 1
        return ans
        
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
 
        return res
s = Solution()
print(s.reverseBits(43261596))
