
from itertools import groupby

class Solution:
    def countAndSay(self, n: int) -> str:
        
        # helper to get rle of some string x
        def rle(x):
            groups = groupby(x)
            res = ""
            for k, g in groups:
                res += str(len(list(g))) + str(k)
            return res

        
        ans = "1"
        for i in range(n-1):
            ans = rle(ans)
        return ans



