def shell_sort(arr):
    n = len(arr)
    gap = n//2
    while gap > 0:
        for i in range (gap,n):
            t = arr[i]
            j = i
            while j >= gap and arr[j - gap] > t:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = t
        gap //= 2
a = [12, 54, 78, 36, 11, 77]
shell_sort(a)
print(a)