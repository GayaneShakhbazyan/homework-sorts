def interpolation_search(arr, key):
    n = len(arr)
    low = 0
    high = n - 1
    while low <= high and key >= arr[low] and key <= arr[high]:
        if arr[high] == arr[low]:
            return low if arr[low] == key else -1
        fraction = (key - arr[low]) / (arr[high] - arr[low])
        pos = low + int(fraction * (high - low))
        if arr[pos] == key:
            return pos
        if arr[pos] < key:
            low = pos + 1 
        else:
            high = pos - 1 
            
    return -1 


a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
target = 100

print(f"Տվյալների ցանկը: {a}")
print(f"Փնտրվող արժեքը (Key): {target}")

index = interpolation_search(a, target)
if index != -1:
    print(f" Գտնվեց: '{target}' արժեքը գտնվում է {index} ինդեքսում։")
else:
    print(f" Չգտնվեց: '{target}' արժեքը չկա ցանկում։")
    
target_mid = 40
index_mid = interpolation_search(a, target_mid) 
print(f"\nՓնտրում ենք '{target_mid}' արժեքը։")
if index_mid != -1:
    print(f" Գտնվեց: '{target_mid}' արժեքը գտնվում է {index_mid} ինդեքսում։")
else:
    print(f" Չգտնվեց: '{target_mid}' արժեքը չկա ցանկում։")