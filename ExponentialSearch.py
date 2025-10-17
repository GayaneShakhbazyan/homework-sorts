def binary_search_part(arr, low, high, key):
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1
def exponential_search(arr, key):
    n = len(arr)
    if arr[0] == key:
        return 0
    i = 1 
    while i < n and arr[i] <= key:
        i = i * 2 
    low = i // 2
    high = min(i, n - 1) 
    
    print(f"որոնման շրջանակը՝ [{low}, {high}]")
    
    return binary_search_part(arr, low, high, key)
my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
search_key = 13

print(f"Տվյալների ցանկը: {my_array}")
print(f"Փնտրվող արժեքը (Key): {search_key}")

index = exponential_search(my_array, search_key)
if index != -1:
    print(f"Գտնվեց: '{search_key}' արժեքը գտնվում է {index} ինդեքսում։")
else:
    print(f"Չգտնվեց: '{search_key}' արժեքը չկա ցանկում։")