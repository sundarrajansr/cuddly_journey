def print_result(source, result, expected):
    print("problem = ", end=' ')
    print(source, end=' ')
    print("result = ", end=' ')
    print(result == expected)


class Solution:
    def search_range(self, nums: list[int], target: int) -> list[int]:
        index = self.binary_search(nums, target, 0, len(nums) - 1)
        if index == -1:
            return [-1, -1]
        return [self.left_boundary(nums, target, index), self.right_boundary(nums, target, index)]

    def binary_search(self, nums: list[int], target: int, left: int, right: int) -> int:
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1

    def left_boundary(self, nums: list[int], target: int, pos: int) -> int:
        cur = pos
        while True:
            if cur - 1 < 0:
                return cur  # beyond array limit. as pos points to target i.e the start index.
            if nums[cur - 1] != target:
                return cur  # one lesser position is a different num than target, hence this is left boundary.
            cur = self.binary_search(nums, target, 0, cur - 1)

    def right_boundary(self, nums: list[int], target: int, pos: int) -> int:
        cur = pos
        while True:
            if cur + 1 >= len(nums):
                return cur
            if nums[cur + 1] != target:
                return cur
            cur = self.binary_search(nums, target, cur + 1, len(nums) - 1)


solution = Solution()
print_result([8, 8, 8, 8, 8, 8, 8, 9], solution.search_range([8, 8, 8, 8, 8, 8, 8, 9], 8), [0, 6])
print_result([2, 3, 3, 3, 8, 8, 8, 9], solution.search_range([2, 3, 3, 3, 8, 8, 8, 9], 3), [1, 3])
print_result([8, 8, 8, 8, 8, 8, 8, 8], solution.search_range([8, 8, 8, 8, 8, 8, 8, 8], 8), [0, 7])
print_result([8, 8, 8, 8, 8, 8, 8, 8], solution.search_range([8, 8, 8, 8, 8, 8, 8, 8], 5), [-1, -1])
print_result([1, 8, 8, 8, 8, 8, 8, 2], solution.search_range([1, 8, 8, 8, 8, 8, 8, 2], 8), [1, 6])
