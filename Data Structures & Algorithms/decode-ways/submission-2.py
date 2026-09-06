class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        n = len(s)
        dp = [0] * 3
        dp[0], dp[1] = 1, 1 if s[0] in '123456789' else 0
        for i in range(2, n+1):
            dp[i%3] = 0
            if s[i-1] in '123456789':
                dp[i%3] += dp[(i-1)%3] 
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i%3] += dp[(i-2)%3] 
        return dp[n%3]
