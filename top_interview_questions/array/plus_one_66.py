from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = False

        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
                carry = True
            else:
                digits[i] += 1
                carry = False
                break;

        if carry:
            digits.insert(0, 1)

        return digits


s = Solution()
print(s.plusOne([1,2,3]))
print(s.plusOne([9]))

