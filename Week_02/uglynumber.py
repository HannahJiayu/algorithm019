class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1] * n 
        a = b = c = 0
        for i in range(1,n): 
            n_2 = dp[a] * 2
            n_3 = dp[b] * 3
            n_5 = dp[c] * 5
            dp[i] = min(n_2, n_3, n_5)
            if n_2 == dp[i]:
                a += 1
            if n_3 == dp[i]:
                b += 1
            if n_5 == dp[i]:
                c += 1
        return dp[n-1]