import numpy as np

def strassen_2x2(A, B, show_steps=False):
    a, b, c, d = A[0,0], A[0,1], A[1,0], A[1,1]
    e, f, g, h = B[0,0], B[0,1], B[1,0], B[1,1]

    P1 = a * (f - h)
    P2 = (a + b) * h
    P3 = (c + d) * e
    P4 = d * (g - e)
    P5 = (a + d) * (e + h)
    P6 = (b - d) * (g + h)
    P7 = (a - c) * (e + f)

    C11 = P5 + P4 - P2 + P6
    C12 = P1 + P2
    C21 = P3 + P4
    C22 = P5 + P1 - P3 - P7

    if show_steps:
        print("\n (P1–P7):")
        for i, p in enumerate([P1, P2, P3, P4, P5, P6, P7], start=1):
            print(f"P{i} = {p}")

    return np.array([[C11, C12],
                     [C21, C22]], dtype=int)


def print_matrix_nicely(matrix, name):
    print(f"\n{name}:")
    for row in matrix:
        print("  ".join(f"{x:5}" for x in row))
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])
print_matrix_nicely(A, "Մատրից A")
print_matrix_nicely(B, "Մատրից B")

C = strassen_2x2(A, B, show_steps=True)
print_matrix_nicely(C, "ԱՐԴՅՈՒՆՔ Մատրից C (A @ B)")
