def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    if len(arr) == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        return arr

    pivot = arr[-1]
    partition = 1
    if arr[0] > arr[1]:
        arr[0], arr[1] = arr[1], arr[0]
    for i in range(2, len(arr)-1):
        if arr[i] < pivot:
            arr[i], arr[partition] = arr[partition], arr[i]
            partition += 1
    arr[partition], arr[-1] = arr[-1], arr[partition]
    return quick_sort(arr[:partition]) + [arr[partition]] + quick_sort(arr[partition+1:])

print(quick_sort([5, 1, 4, 2, 8, 3, 7, 6, 9, 0, 4, 2]))