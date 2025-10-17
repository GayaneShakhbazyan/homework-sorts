def ternary_search(arr, key):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3
        
        if arr[mid1] == key:
            return mid1
        if arr[mid2] == key:
            return mid2
        
        if key < arr[mid1]:
            high = mid1 - 1 
        elif key > arr[mid2]:
            low = mid2 + 1  
        else:
            low = mid1 + 1  
            high = mid2 - 1

    return 0
sorted_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
t = 7

index = ternary_search(sorted_data, t)
if index != 0:
    print(f"'tivy {t}'index {index}")
else:
    print(f"'{t}'error")
