class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sc = [0 for _ in range(26)]
        tc = [0 for _ in range(26)]
        
        for c in s:
            sc[ord(c)-97] += 1
        for c in t:
            tc[ord(c)-97] += 1
        
        for i in range(26):
            if sc[i] != tc[i]:
                return False
        return True

        
