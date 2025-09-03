class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle): 
            return -1
        for i in range(len(haystack)):
            j = i
            k = 0

            # if there is not enough characters left to compare, return -1 
            if len(needle) > len(haystack) - i:
                return -1
            else:
                # compare - if match return i, else continue
                while k < len(needle):
                    if haystack[j] != needle[k]:
                        break
                    k += 1
                    j += 1
                if k == len(needle):
                    return i

        return -1

s = Solution()
print(s.strStr("sadbutsad", "sad"))
print(s.strStr("leetcode", "leeto"))
