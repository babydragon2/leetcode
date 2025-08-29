from typing import List
from collections import defaultdict

# worked but was very slow - took some time to debug (23min total, 37min with debug)
# key optimizations include only one double loop (keep track of rows, cols, and boxes as you go)
# for boxes, key the dictionary by box number, this can be done multiple ways (use floor, or calculate the number)
class Solution1:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRows(b) -> bool:
            for i in range(9):
                d = {}
                for j in range(9):
                    if board[i][j] != "." and board[i][j] in d:
                        return False
                    d[board[i][j]] = True

            return True

        def checkCols(b) -> bool:
            for i in range(9):
                d = {}
                for j in range(9):
                    if board[j][i] != "." and board[j][i] in d:
                        return False
                    d[board[j][i]] = True

            return True

           
        def checkChunks(b) -> bool:
            inits = [(0, 0), (0, 3), (0, 6), (3, 0), (6, 0), (3, 3), (3, 6), (6, 6), (6, 3)]
            for x,y in inits:
                d = {}
                print("chunk", x, y)
                for i in range(x, x+3):
                    for j in range(y, y+3):
                        print(i, j, board[i][j])
                        if board[i][j] != "." and board[i][j] in d:
                            return False
                        d[board[i][j]] = True

            return True


        return checkChunks(board) and checkRows(board) and checkCols(board)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_d = defaultdict(set)
        cols_d = defaultdict(set)
        boxes_d = defaultdict(set)

        for r in range(9):
            for c in range(9):
                e = board[r][c]
                if e == ".":
                    continue
                
                if e in rows_d[r] or e in cols_d[c] or e in boxes_d[(r//3, c//3)]:
                    return False
                rows_d[r].add(e)
                cols_d[c].add(e)
                boxes_d[(r//3, c//3)].add(e)
        return True
                 

s = Solution()

print(s.isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))




