class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        dp = [[float('-inf') for _ in range(col)] for _ in range(row)]
        dp[row - 1][col - 1] = grid[row - 1][col - 1]
        for i in range(col - 2, -1, -1):
            dp[row - 1][i] = dp[row - 1][i + 1] + grid[row - 1][i]
        for i in range(row - 2, -1, -1):
            dp[i][col - 1] = dp[i + 1][col - 1] + grid[i][col - 1]
        for i in range(row - 2, -1, -1):
            for j in range(col - 2, -1, -1):
                dp [i][j] = min(dp[i + 1][j], dp[i][j + 1]) + grid[i][j]
        return dp[0][0]
