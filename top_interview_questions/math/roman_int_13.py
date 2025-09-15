class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ans = 0

        # traverse from right to left (should be inc), if not increasing, subtract in 
        n = len(s)-1
        ans += d[s[n]]

        i = n
        j = i-1
        while j >= 0:
            # print("i: ", i, "j: ", j, "d[s[j]]: ", d[s[j]], "d[s[i]]: ", d[s[i]], "ans: ", ans)
            if d[s[j]] < d[s[i]]:
                ans -= d[s[j]]
            else:
                ans += d[s[j]]
            i -= 1
            j -= 1

        return ans


s = Solution()
print(s.romanToInt("LVIII"))

