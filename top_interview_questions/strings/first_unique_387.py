class Solution1:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in range(len(s)):
            c = s[i]
            if c in d:
                d[c] = (d[c][0] + 1, d[c][1])
            else:
                d[c] = (1, i)

        min_idx = -1
        for _, v in d.items():
            if v[0] == 1:
                if min_idx == -1:
                    min_idx = v[1]
                else:   
                    min_idx = min(min_idx, v[1])
        return min_idx


class Solution:
    def firstUniqChar(self, s: str) -> int:
        # optimized solution with queue to avoid 2nd pass 
        d = {}
        q = []

        for i in range(len(s)):
            c = s[i]
            if c not in d:
                d[c] = 1
                q.append(i)
            else:
                d[c] += 1
        
        while len(q) and d[s[q[0]]] > 1:
            q.pop(0)
        
        return q[0] if len(q) else -1   
 
s = Solution()
print(s.firstUniqChar("loveleetcode"))
print(s.firstUniqChar("aabb"))
        
