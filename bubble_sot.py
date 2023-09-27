def bubble_sort(arr):
    n = len(arr)

    for j in range(n-1, 0, -1):
        for i in range(j):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


print(bubble_sort([5, 1, 4, 2, 8]))