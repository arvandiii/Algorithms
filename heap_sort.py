def heap_sort(arr):
    if len(arr) == 1:
        return arr
    for i in range(len(arr)//2 - 1, -1, -1):
        heapify(arr, i)
    
    max = arr[0]
    new_arr = arr[1:]
    return heap_sort(new_arr) + [max]


def heapify(arr, i):
    l, r = (i * 2) + 1, (i * 2) + 2
    largest = i
    if l < len(arr) and arr[l] > arr[i]:
        largest = l
    if r < len(arr) and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, largest)

print(heap_sort([1, 3, 5, 2, 4, 6, 7, 9, 8]))

