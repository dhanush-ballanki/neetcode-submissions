class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0]*(n+3)
        dp[n-1] = stoneValue[n-1]
        neg_inf = float('-inf')
        for i in range(n-1, -1, -1):
            one = stoneValue[i] - dp[i+1]
            two, three = neg_inf, neg_inf
            if i + 1 < n:
                two = stoneValue[i] + stoneValue[i+1] - dp[i+2]
            if i + 2 < n:
                three = stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - dp[i+3]
            dp[i] = max(one, two, three)
        if dp[0] > 0:
            return 'Alice'
        elif dp[0] < 0:
            return 'Bob'
        else:
            return 'Tie'
