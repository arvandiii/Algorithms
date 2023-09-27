def insersion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        for j in range(i-1, -1, -1):
            if arr[j] <= key:
                break
            arr[j+1], arr[j] = arr[j], arr[j+1]

            
    return arr

print(insersion_sort([5, 1, 4, 2, 8]))
