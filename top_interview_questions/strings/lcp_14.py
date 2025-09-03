from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = strs[0]

        for i in range(1, len(strs)):
            # build new lcp and assign it to lcp, if "" return
            newlcp = ""
            compstr = strs[i]
            for j in range(min(len(lcp), len(compstr))):
                if lcp[j] == compstr[j]:
                    newlcp += compstr[j]
                else:
                    break
            if newlcp == "":
                return ""
            else:
                lcp = newlcp

        return lcp

s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]), "fl")
print(s.longestCommonPrefix(["dog","racecar","car"]), "")


        
