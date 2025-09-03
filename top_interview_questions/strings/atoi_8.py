class Solution:
    def myAtoi(self, s: str) -> int:
        # strip whitespace 
        s = s.strip()
        if not len(s):
            return  0
        
        # get sign and strip leading 0's, the sign should come first
        neg  = s[0] == '-'
        s = s[1:] if s[0] == '+' or s[0] == '-' else s
        s = s.lstrip('0')

        digits = ""
        # read digits until a non-digit is read 
        for c in s:
            if c.isnumeric():
                digits += c
            else:
                break

        if len(digits) == 0:
            return 0
        
        # check bound constraints and round if needed
        n = len(digits)
        if n > 10:
            if neg:
                return -2 ** 31
            else:
                return 2 ** 31 -1
        elif n < 10:
            if neg:
                return -1 * int(digits)
            else:
                return int(digits)
        else:
            if neg:
                if digits > str(2**31):
                    return -2**31
                else:
                    return -1*int(digits)
            else:
                if digits > str(2**31-1):
                    return 2**31-1
                else:
                    return int(digits)
    

s = Solution()

print(s.myAtoi("42"), 42)
print(s.myAtoi("-42"), -42)
print(s.myAtoi("0042"), 42)
print(s.myAtoi("1337c0d3"), 1337)
print(s.myAtoi("0-1"), 0)
print(s.myAtoi("words and 987"), 0)
print(s.myAtoi("+-12"), 0)
print(s.myAtoi("-2147483649"), "-2147483648")
            



        
        
