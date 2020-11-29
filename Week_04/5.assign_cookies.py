class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not g or not s:
            return 0
        g.sort()
        s.sort()
        i = j = 0
        cnt = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                cnt += 1
                i += 1
            j += 1
        return cnt
