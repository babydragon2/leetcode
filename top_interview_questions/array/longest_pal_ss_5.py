
# Brute Force - TLE o(n^3)
class Solution1:
    def longestPalindrome(self, s: str) -> str:
        ans = s[0] 

        def ispal(x):
            l = 0
            r = len(x)-1
            while l < r:
                if x[l] != x[r]:
                    return False
                l += 1
                r -= 1
            return True

        for i in range(len(s)):
            for j in range(i+1, len(s)):
                substr = s[i:j+1]
                if ispal(substr):
                    if len(substr) > len(ans):
                        ans = substr

        return ans 


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # what is easier to consider? All substrings, or all palindromes?
        # There are n^2 substrings, but only 2n-1 possible palindromes (n odd centers and n-1 even centers)
        # Therefore we can reduce O(n^3) to O(n^2)
        
        ans = s[0]

        def getpal(l, r):
            # return the longest palindrome in the bounds l and r
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]


        for i in range(len(s)):
            pal1 = getpal(i, i) # center starts on a single index (odd center)
            pal2 = getpal(i, i+1) # center starts on two indexes (even center)
            if len(ans) < len(pal1):
                ans = pal1
            if len(ans) < len(pal2):
                ans = pal2  
        return ans


 
s = Solution()
print(s.longestPalindrome("babad"))
print(s.longestPalindrome("cbbd"))
print(s.longestPalindrome("bb"))
