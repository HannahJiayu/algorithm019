class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0:
            return []
        def generateBoard():
            boardlist = []
            for i in range(len(queen)):
                printRow[queen[i]] = 'Q'
                boardlist.append(''.join(printRow))
                printRow[queen[i]] = '.'
            return boardlist
        def solve(row, col, pie, na):
            if row == n:
                solution.append(generateBoard())
            else:
                availablePosition = ((1 << n) - 1) & (~(col | pie | na))
                while availablePosition:
                    position = availablePosition & -availablePosition
                    availablePosition = availablePosition & (availablePosition - 1)
                    column = bin(position - 1).count('1')
                    queen[row] = column
                    solve(row + 1, col | position, (pie | position) >> 1, (na | position) << 1)
        
        solution = []
        printRow = ['.'] * n
        queen = [-1] * n
        solve(0, 0, 0, 0)
        return solution

