import math
def jump_search(arr, k):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while arr[min(step, n) - 1] < k:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    while arr[prev] < k:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[prev] == k:
        return prev
    return -1
a = [0, 1, 18, 2, 3, 58, 8, 13, 21, 34, 55, 89, 144, 233]
t = 21

print(f"Ցանկ (N={len(a)}): {a}")
print(f"Փնտրվող արժեքը (K): {t}")
index = jump_search(a, t)
if index != -1:
    print(f"\n '{t}' արժեքը գտնվում է {index} ինդեքսում։")
else:
    print(f"\n '{t}' արժեքը չկա ցանկում։")
t_not_found = 100
index_not_found = jump_search(a, t_not_found)

print(f"\n Գտնել արժեքը '{t_not_found}' արժեքը։")
if index_not_found != -1:
    print(f"'{t_not_found}' արժեքը գտնվում է {index_not_found} ինդեքսում։")
else:
    print(f" '{t_not_found}' արժեքը չկա ցանկում։")