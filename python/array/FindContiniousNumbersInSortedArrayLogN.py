class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        index = self.binarySearch(nums, target, 0, len(nums)-1)
        if index == -1:
            return [-1, -1]
        return [self.leftBoundary(nums, target, index), self.rightBoundary(nums, target, index)]
    def binarySearch(self, nums: list[int], target: int, left: int, right: int) -> int:
        while left < right:
            mid = (right + left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1
    def leftBoundary(self, nums: list[int], target: int, pos: int) -> int:
        cur = pos
        while True:
            if cur - 1 < 0:
                return cur # beyond array limit. as pos points to target i.e the start index.
            if nums[cur - 1] != target:
                return cur # one lesser position is a different num than target, hence this is left boundary.
            cur = self.binarySearch(nums, target, 0, cur - 1)
    def rightBoundary(self, nums: list[int], target: int, pos: int) -> int:
        cur = pos
        while True:
            if cur + 1 >= len(nums):
                return cur
            if nums[cur + 1] != target:
                return cur
            cur = self.binarySearch(nums, target, cur + 1, len(nums) - 1)
soln = Solution()
print(soln.searchRange([8, 8, 8, 8, 8, 8, 8, 9], 8))