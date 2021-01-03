class Solution:
    def firstUniqChar(self, s: str) -> int:
        charmap = collections.Counter(s)
        index = 0
        for char in s:
            if charmap[char] == 1:
                return index
            else:
                index += 1
        return -1