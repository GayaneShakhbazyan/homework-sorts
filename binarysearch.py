def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2 
        
        if arr[mid] == key:
            return mid 
        elif arr[mid] < key:
            low = mid + 1  
        else:
            high = mid - 1 

    return 0

sorted_data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
t = 40

index = binary_search(sorted_data, t)
if index != 0:
    print(f"'tivy {t} index {index}")
else:
    print(f"'{t}' error")
