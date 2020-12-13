class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        dp = [[False] * len(s) for _ in range(len(s))]
        for j in range(len(s)):
            for i in range(len(s)):
                if i == j:
                    dp[i][j] = True
                    cnt += 1
                elif j - i == 1:
                    if s[i] == s[j]:
                        dp[i][j] = True
                        cnt += 1
                elif j - i > 1 and s[i] == s[j] and dp[i+1][j-1]:
                        dp[i][j] = True
                        cnt += 1
        return cnt


