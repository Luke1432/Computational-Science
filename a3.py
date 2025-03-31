import numpy as np

# Given matrix A and vector b
A = np.array([[2.4343, 2.87674, 2.2122],
              [3.1454, 3.49564, 1.7512],
              [3.5309, 3.10174, -2.1358]])

b = np.array([4.5, -9.5, 2.0])

# Perform LU decomposition with partial pivoting manually
n = len(A)
P = np.eye(n)  # Identity matrix for permutation
L = np.eye(n)  # Lower triangular matrix
U = A.copy()   # Upper triangular matrix

for i in range(n):
    # Pivoting: Find the maximum element in the current column
    max_row = np.argmax(np.abs(U[i:, i])) + i
    if i != max_row:
        # Swap rows in U
        U[[i, max_row]] = U[[max_row, i]]
        # Swap rows in P
        P[[i, max_row]] = P[[max_row, i]]
        if i > 0:
            # Swap rows in L (only the left part up to column i)
            L[[i, max_row], :i] = L[[max_row, i], :i]

    # Perform elimination
    for j in range(i + 1, n):
        factor = U[j, i] / U[i, i]
        L[j, i] = factor
        U[j] -= factor * U[i]

# Solve the system using LU decomposition
Pb = P @ b

# Forward substitution to solve Ly = Pb
y = np.zeros(n)
for i in range(n):
    y[i] = Pb[i] - np.dot(L[i, :i], y[:i])

# Backward substitution to solve Ux = y
x = np.zeros(n)
for i in range(n - 1, -1, -1):
    x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]

# Check errors
PA = P @ A
LU = L @ U
pa_lu_error = np.linalg.norm(PA - LU)
ax_b_error = np.linalg.norm(A @ x - b)

print("Permutation Matrix (P):\n", P)
print("Lower Triangular Matrix (L):\n", L)
print("Upper Triangular Matrix (U):\n", U)
print("Solution x:\n", x)
print("Error in PA = LU:", pa_lu_error)
print("Error in Ax = b:", ax_b_error)
