class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {')': '(', ']': '[', '}':'{'}

        for c in s:
            if c not in d:
                stack.append(c)
            else:
                if len(stack):
                    top = stack.pop()
                    if top != d[c]:
                        return False
                else:
                    return False

        return len(stack) == 0

        
