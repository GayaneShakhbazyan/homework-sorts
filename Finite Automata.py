def check_ab(s):
    state = 0 
    for char in s:
        if state == 0:
            if char == 'a':
                state = 1
        elif state == 1:
            if char == 'b':
                state = 2
            elif char == 'a':
                state = 1
            else:
                state = 0
    return state == 2

print(f"abac-ը պարունակում է? 'ab': {check_ab('abac')}") 
print(f"baac-ը պարունակում է? 'ab': {check_ab('baac')}")