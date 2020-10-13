# https://www.hackerrank.com/challenges/max-array-sum/problem
# Same as house robber problem where he cannot rob consecutive houses, but with huge no of negative sum many cases fails.
# Complete the maxSubsetSum function below.
def maxSubsetSum(nums):
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])
    a = nums[0]
    b = max(a, nums[1])
    for i in range(2, len(nums)):
        b, a = max(nums[i],nums[i] + a, b), b
    return b


def main():
    res = maxSubsetSum([-2, -1, -3, -1, 1, 0, -2, 3, 1, 0, -1, 1, -1])
    print(res)


main()
