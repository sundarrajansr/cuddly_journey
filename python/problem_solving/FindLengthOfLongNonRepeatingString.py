# https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0: return 0

        charMap = {}
        i = 0
        maxSoFar = 0
        uniqueFrom = 0

        while (i < n):
            if s[i] in charMap:
                maxSoFar = max(maxSoFar, len(charMap))
                j = charMap[s[i]]
                for k in range(uniqueFrom,j):
                    del charMap[s[k]] # delete only chars till last non-unique i.e reuse the existing map for count
                uniqueFrom = j + 1
            charMap[s[i]] = i
            i += 1

        return max(maxSoFar, len(charMap))


print(Solution().lengthOfLongestSubstring("dvdfvabd"))
