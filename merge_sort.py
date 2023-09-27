def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    a1 = merge_sort(arr[:len(arr)//2])
    a2 = merge_sort(arr[len(arr)//2:])
    return merge(a1, a2)
    

def merge(arr1, arr2):
    new_arr = []
    i, j = 0, 0
    while True:
        if i == len(arr1):
            new_arr += arr2[j:]
            break
        if j == len(arr2):
            new_arr += arr1[i:]
            break
        if arr1[i] <= arr2[j]:
            new_arr.append(arr1[i])
            i += 1
        else:
            new_arr.append(arr2[j])
            j += 1
    return new_arr
    

print(merge_sort([5, 1, 4, 2, 8, 3, 7, 6, 9, 0, 4, 2]))