from typing import List

# Backtracking DFS - O(mn) time w/ recursive stack space O(mn)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def helper(i, j):
            grid[i][j] = "#"
            if i+1 < rows and grid[i+1][j] == '1':
                helper(i+1, j)
            if i-1 >= 0 and grid[i-1][j] == '1':
                helper(i-1, j)
            if j-1 >= 0 and grid[i][j-1] == '1':
                helper(i, j-1)
            if j+1 < cols and grid[i][j+1] == '1':
                helper(i, j+1)

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    helper(r, c)

        return count
