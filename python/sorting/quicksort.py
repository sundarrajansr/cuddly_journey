def quick_sort(nums, lo, hi):
    if lo >= hi:
        return
    q = partition(nums, lo, hi)
    quick_sort(nums, lo, q - 1)
    quick_sort(nums, q + 1, hi)


def partition(nums, lo, hi):
    if lo >= hi:
        return
    pivot = nums[hi]
    i = -1
    j = hi
    for k in range(lo, hi - 1):
        if nums[k] < pivot:
            nums[k], nums[i + 1] = nums[i + 1], nums[k]
            i += 1
        else:
            nums[k], nums[j - 1] = nums[j - 1], nums[k]
            j = j - 1
    nums[i + 1] = pivot
    return i + 1


arr = [1,8,2,3,4,10,12,7,6]
quick_sort(arr,0,len(arr)-1)
print(arr)
