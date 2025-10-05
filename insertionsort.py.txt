def insertion_sort(arr):
    for i in range(1, len(arr)):
        k = arr[i]        
        j = i - 1
        while j >= 0 and arr[j] > k:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = k
    return arr
n = [1, 64, 14, 21, 3]
print(insertion_sort(n))
