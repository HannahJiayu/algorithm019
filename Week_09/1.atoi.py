class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0: return 0
        index, sign, num = 0, 1, 0
        while index < len(s) and s[index] == ' ':
            index += 1
        if index < len(s) and (s[index] == '-' or s[index] == '+'):
            if s[index] == '-':
                sign = -1
            index += 1
        while index < len(s) and s[index].isdigit():
            num = 10 * num + ord(s[index]) - ord('0')
            index += 1
        return max(-(1 << 31), min(sign * num,(1 << 31)-1))