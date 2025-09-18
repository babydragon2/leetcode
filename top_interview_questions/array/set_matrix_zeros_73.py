from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """


        r = len(matrix)
        c = len(matrix[0])

        i = 0
        while i < r:
            j = 0
            while j < c:
                if matrix[i][j] == 0:
                    # mark the entire row
                    for k in range(r):
                        if matrix[k][j] == 0:
                            continue
                        else:
                            matrix[k][j] = 2**32 
                    # zero out the entire col
                    for k in range(c):
                        if matrix[i][k] == 0:
                            continue
                        else:
                            matrix[i][k] = 2**32
                j += 1
            i += 1


        i = 0
        while i < r:
            j = 0
            while j < c:
                if matrix[i][j] == 2**32:
                    matrix[i][j] = 0
                j += 1
            i += 1

        print(matrix)
        

s = Solution()
s.setZeroes([[1,1,1],[1,0,1],[1,1,1]])
