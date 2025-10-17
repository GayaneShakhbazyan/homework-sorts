def quick_sort(arr):
    pivot = arr[0]  
    left = []      
    right = []      

    for x in arr[1:]:  
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)
    return left, pivot, right
def quick_s(arr):
    if len(arr) <= 1:
        return arr
    left, pivot,right = quick_sort(arr)
    return quick_s(left) + [pivot] + quick_s(right)
n = [6, 27, 46, 21, 1]
print(quick_s(n))

