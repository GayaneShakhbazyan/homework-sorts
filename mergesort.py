def merge_sort(arr):
    if len(arr) <= 1:  
        return arr

    mid = len(arr) // 2         
    left = merge_sort(arr[:mid]) 
    right = merge_sort(arr[mid:])
    return merge(left, right)
def merge(left, right):
    m = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            m.append(left[i])
            i += 1
        else:
            m.append(right[j])
            j += 1
    m.extend(left[i:])
    m.extend(right[j:])
    return m
n = [6, 38, 72, 24, 18]
print(merge_sort(n))
