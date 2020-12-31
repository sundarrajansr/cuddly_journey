# https://leetcode.com/problems/string-to-integer-atoi/
# medium
#
class Solution:
    def myAtoi(self, s: str) -> int:
        total = 0
        negative = False
        for c in s:
            if c in [' ', '.', '+']:
                continue
            if c == '-':
                if total == 0:
                    negative = True
                else:
                    return 0
            v = ord(c)
            if 48 >= v <= 57:
                v -= 48
                total += (total * 10) + v
            else:
                break
        return total


s = Solution()
print(s.myAtoi('   -342423 word'))
