class Solution:
    def totalNQueens(self, n: int) -> int:
        if n == 0:
            return 0
        def dfs(row, col, pie, na):
            if row == n:
                return 1
            else:
                count = 0
                availablePosition = ((1 << n)-1) & (~(col | pie | na))
                while availablePosition:
                    position = availablePosition & -availablePosition
                    availablePosition = availablePosition & (availablePosition - 1)
                    count += dfs(row + 1, col | position, (pie | position) >> 1, (na | position) << 1)
                return count
            
        return dfs(0, 0, 0, 0)