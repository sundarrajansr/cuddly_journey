# https://leetcode.com/problems/string-to-integer-atoi/
# medium
#
class Solution:
    def myAtoi(self, s: str) -> int:
        total = 0
        for c in s:
            if c == ' ':
                continue
            if c == '.':
                continue
            v = ord(c)
            if 48 <= v <= 57:
                v -= 48
                total = (total * 10) + v
            else:
                break
        return total
