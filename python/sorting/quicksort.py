def quick_sort(nums, lo, hi):
    if lo < hi:
        q = partition(nums, lo, hi)
        quick_sort(nums, lo, q - 1)
        quick_sort(nums, q + 1, hi)
    else:
        return


def partition(nums, lo, hi):
    pivot = nums[hi]
    i = lo-1
    for k in range(lo, hi):
        if nums[k] < pivot:
            i += 1
            nums[k], nums[i] = nums[i], nums[k]
    nums[i + 1], nums[hi] = pivot, nums[i + 1]
    return i + 1


arr = [2,2,2,4,4,6,5,5,7]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
