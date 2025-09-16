from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        q = []
        ans = []
        i = 1

        while i <= numRows:
            if not q:
                q = [[1]]

            row = q.pop(0)
            ans.append(row)

            new_row = []
            new_row.append(row[0])

            for j in range(len(row)-1):
                new_row.append(row[j]+row[j+1])

            new_row.append(row[-1])
            q.append(new_row)


            i += 1

        return ans

s = Solution()
print(s.generate(1))
print(s.generate(2))
print(s.generate(3))
print(s.generate(4))
