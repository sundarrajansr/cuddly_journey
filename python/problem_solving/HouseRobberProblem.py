# https://www.hackerrank.com/challenges/max-array-sum/problem
#
# Same as house robber problem but negative values present in array makes it even more interesting.
# choose maximum of arr[n] + f(n-2), f(n-1), arr[n]
# it differs from house robber problem by the fact it includes negative cost
#
# also select current array index if prev choice includes a neg cost.
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
        b, a = max(nums[i], nums[i] + a, b), b
    return b


def main():
    res = maxSubsetSum([-2, 1, 3, -4, 5])
    print(res)


main()
