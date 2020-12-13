class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        pre = now = 1
        for i in range(1, len(s)):
            tmp = now
            if s[i] == '0':
                if s[i-1] == '1' or s[i-1] == '2':
                    now = pre
                else:
                    return 0
            else:
                if s[i-1] == '1' or (s[i-1] == '2' and s[i] >= '1' and s[i] <= '6'):
                    pre, now = now, pre + now
            pre = tmp
        return now