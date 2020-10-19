# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/561/week-3-october-15th-october-21st/3497/

# Search a 2D Matrix


def searchMatrix(matrix, target) -> bool:
    row = len(matrix)
    col = len(matrix[0])
    return True
    pass


class Solution:

    # corner case : arr should not have duplicate keys - is Fixed by using the invariant now :)
    #
    def binary_search_exact_or_lesser(self, arr, lo, hi, v):
        if lo > hi:
            return arr[max(0,lo-1)]
        mid = (lo + hi) // 2
        if arr[mid] == v:
            return arr[mid]
        if arr[mid] > v:
            return self.binary_search_exact_or_lesser(arr, lo, mid - 1, v)
        else:
            return self.binary_search_exact_or_lesser(arr, mid + 1, hi, v)
        pass


s = Solution()
arr = [1,1,1,1,2,3,4,4,4,4,5,6,7,9,12,12,12,12,12,12]
print(arr)
x = s.binary_search_exact_or_lesser(arr, 0, len(arr) - 1, 6)
print(f'val is {x}')
