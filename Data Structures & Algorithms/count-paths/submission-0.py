class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 if (i == n-1 or j == m-1) else 0 for i in range(n)] for j in range(m)]
        for r in range(m-2, -1, -1):
            for c in range(n-2, -1, -1):
                dp[r][c] = dp[r+1][c] + dp[r][c+1]
        return dp[0][0]