from tabulate import tabulate

compares = 0
arr_access = 0
arr_updates = 0
swaps = 0


def less(a, b):
    globals()['compares'] += 1
    return a < b


def exchange(a, b):
    globals()['swaps'] += 1
    a, b = b, a


def get_arr_val(arr, index):
    if 0 <= index < len(arr):
        globals()['arr_access'] = globals()['arr_access'] + 1
        return arr[index]
    else:
        return None


def update_arr(arr, index, val):
    if 0 <= index < len(arr):
        globals()['arr_updates'] += 1
        arr[index] = val


def insertion_sort(arr, n):
    for i in range(1, n):
        pivot = get_arr_val(arr, i)
        j = i - 1
        while j >= 0 and less(pivot, get_arr_val(arr, j)):
            update_arr(arr, j + 1, get_arr_val(arr, j))
            j -= 1
        if j != i - 1:
            update_arr(arr, j + 1, pivot)


def selection_sort(arr: list, n: int) -> list:
    if n == 0: return arr

    for i in range(n):
        min_val = get_arr_val(arr, i)
        for j in range(i + 1, n):
            j_val = get_arr_val(arr, j)
            if less(j_val, min_val):
                min_val = j_val
        update_arr(arr, i, min_val)
    return arr

    pass


def TestSort(fn):
    descending_arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    average_arr = [1, 4, 9, 2, 4, 5, -1, 3]
    sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    duplicates_arr = [1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 5, 1, 2, 3, 6, 7, 2, 3, 4, 4]

    pass


# nums = [1, 4, 9, 2, 4, 5, -1, 3]
nums = [1, 4, 9, 2, 4, 5, -1, 3]
print(nums)
selection_sort(nums, len(nums))
print(nums, end='\n\n')
result = [['arr length', len(nums)], ['compare ops', compares], ['read ops', arr_access],
          ['write ops', arr_updates + swaps]]
print(tabulate(result, headers=['sort attributes', 'insertion sort']))
