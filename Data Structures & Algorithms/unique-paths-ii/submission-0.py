class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dp = [[0]*COLS for _ in range(ROWS)]
        if grid[ROWS-1][COLS-1] == 1 or grid[0][0] == 1:
            return 0
        dp[ROWS-1][COLS-1] = 1
        for c in range(COLS - 2, -1, -1):
            if grid[ROWS-1][c] == 0:
                dp[ROWS-1][c] = dp[ROWS-1][c+1]
        
        for r in range(ROWS - 2, -1, -1):
            if grid[r][COLS-1] == 0:
                dp[r][COLS-1] = dp[r+1][COLS-1]
                
        for r in range(ROWS-2, -1, -1):
            for c in range(COLS-2, -1, -1):
                if grid[r][c] == 1:
                    continue
                dp[r][c] = dp[r+1][c] + dp[r][c+1]
        return dp[0][0]