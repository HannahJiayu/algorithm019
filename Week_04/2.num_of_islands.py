class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs_masking(grid, i, j, m, n):
            if i < 0 or j < 0 or i == m or j == n or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            dfs_masking(grid, i-1, j, m, n)
            dfs_masking(grid, i+1, j, m, n)
            dfs_masking(grid, i, j-1, m, n)
            dfs_masking(grid, i, j+1, m, n)

        if len(grid) == 0:
            return 0
        else:
            m, n= len(grid),len(grid[0])
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    cnt += 1
                    dfs_masking(grid, i, j, m, n)
        return cnt