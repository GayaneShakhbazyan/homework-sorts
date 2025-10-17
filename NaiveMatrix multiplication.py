import numpy as np

def numpy_matrix_multiplication(A_list, B_list):
    A = np.array(A_list)
    B = np.array(B_list)
    rows_A, cols_A = A.shape
    rows_B, cols_B = B.shape

    if cols_A == rows_B:
        C = A @ B
        return C
    else:
        print(f"Սխալ: A-ի սյուներ ({cols_A}) != B-ի տողեր ({rows_B})")
        return None

def print_matrix(matrix, name):
    print(f"\n{name}:")
    for row in matrix:
        print('  '.join(f"{x:5}" for x in row))  

A_list = [
    [1, 2, 3],
    [4, 5, 6]
]
B_list = [
    [7, 8],
    [9, 10],
    [11, 12]
]

C_numpy = numpy_matrix_multiplication(A_list, B_list)

print_matrix(A_list, "Մատրից A")
print_matrix(B_list, "Մատրից B")

if C_numpy is not None:
    print_matrix(C_numpy, " Մատրից C (A * B)")
