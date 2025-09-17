from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # transpose the matrix, then reverse the order of the columms
        n = len(matrix)
        for r in range(n):
            for c in range(r+1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
    
        for r in range(n):
            for c in range(n//2):
                matrix[r][c], matrix[r][n-c-1] = matrix[r][n-c-1], matrix[r][c]
        
s = Solution()
s.rotate([[1,2,3],[4,5,6],[7,8,9]])
