def compute_lps_array(x):
    M = len(x)
    lps = [0] * M  
    length = 0      
    i = 1       
    while i < M:
        if x[i] == x[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(text, x):
    N = len(text)
    M = len(x)
    lps = compute_lps_array(x)
    
    i = 0  
    j = 0
    
    print(f"X-ի LPS զանգվածը: {lps}")
    
    while i < N:
        if x[j] == text[i]:
            i += 1
            j += 1
        
        if j == M:
            return i - j
            
        elif i < N and x[j] != text[i]:
            if j != 0:
                j = lps[j - 1] 
            else:
                i += 1
                
    return -1


text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB" 

index = kmp_search(text, pattern)
if index != -1:
    print(f"Տեքստ: {text}")
    print(f"X: {' ' * index}{pattern}")
    print(f" Համընկնումը սկսվում է {index} դիրքից։")
else:
    print(" Համընկնում չգտնվեց։")