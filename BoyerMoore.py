def compute_bad_char_table(pattern):
    M = len(pattern)
    bad_char_table = {}
    for i in range(M):
        bad_char_table[pattern[i]] = i
        
    return bad_char_table


def boyer_moore_search(text, pattern):
    N = len(text)
    M = len(pattern)
    if M == 0 or M > N:
        return -1
    bad_char_table = compute_bad_char_table(pattern)
    
    print(f" {bad_char_table}")
    s = 0 
    while s <= N - M:
        j = M - 1 
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            return s
            
        else:
            mismatch_char = text[s + j]
            last_occurrence_in_pattern = bad_char_table.get(mismatch_char, -1)
            shift = j - last_occurrence_in_pattern
            s += max(1, shift)

    return -1

text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB" 

index = boyer_moore_search(text, pattern)
print(f"Տեքստ: {text}")

if index != -1:
    print(f"Pattern: {' ' * index}{pattern}")
    print(f" Համընկնումը սկսվում է {index} դիրքից։")
else:
    print(" Համընկնում չգտնվեց։")