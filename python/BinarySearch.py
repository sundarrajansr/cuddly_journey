def binarySearch(nums, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if nums[mid] == target:
        return mid
    if nums[mid] > target:
        return binarySearch(nums, target, start, mid - 1)
    else:
        return binarySearch(nums, target, mid + 1, end)


def binarySearchIterative(nums, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


def TestBinarySearch():
    search_fns = [binarySearch, binarySearchIterative]
    test_cases = list()
    test_cases.append([[1, 2, 3, 4, 5, 6, 7, 8], 4, 3])
    test_cases.append([[1, 1, 1, 1, 1, 1, 1, 1], 1, 3])
    test_cases.append([[1, 9, 10], 12, None])
    test_cases.append([[-1, 0, 1], 1, 2])
    test_cases.append([[-4, -3, -2, -1], -2, 2])
    test_cases.append([[0, 0, 0, 0], 1, None])
    for fn in search_fns:
        for test_case in test_cases:
            nums = test_case[0]
            target = test_case[1]
            expected = test_case[2]
            solution = fn(nums, target, 0, len(nums) - 1)
            if expected == solution:
                print(f'PASS :\t {test_case} fn : {fn.__name__} solution : {solution}')
            else:
                print(f'FAIL :\t {test_case} fn : {fn.__name__} solution : {solution}')


TestBinarySearch()
