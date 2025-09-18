from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list) 
        res = []

        for s in strs:
            l = [0]*26
            for c in s:
                l[ord(c)-97] += 1
            key = tuple(l)
            d[key].append(s)
                
        for _, v in d.items():
            res.append(v)

        return res



