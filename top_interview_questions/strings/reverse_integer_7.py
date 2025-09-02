class Solution:
    def reverse(self, x: int) -> int:
        ns = str(x)
        neg = False 
        if ns[0] == "-":
            ns = ns[1:]
            neg = True
         
        ns = ''.join(reversed(ns))
        ns = ns.lstrip("0")
        max_32 = str(2 ** 31 - 1)
        min_32 = str(2 ** 31)
        dig = 10 # more than 10 digits is to much, less is okay, if equal, compare strings
        
        if len(ns) == 0:
            return 0
        if len(ns) > 10:
            return 0
        elif len(ns) < 10:
            return int(ns) * -1 if neg else int(ns)
        else:
            if neg:
                if ns > min_32:
                    return 0
                else:
                    return int(ns) * -1
            else:
                if ns > max_32:
                    return 0
                else:
                    return int(ns)
            

s = Solution()
print(s.reverse(123))
print(s.reverse(-123))
print(s.reverse(12300))
print(s.reverse(-123000))

