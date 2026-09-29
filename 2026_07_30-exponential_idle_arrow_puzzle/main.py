from sympy import Matrix
from math import gcd

# Define system: Ax = b (mod m)

m = 4

A = Matrix([
    [1, 1, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 0, 1, 1, 0, 1, 1],
    [0, 0, 0, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 0, 1, 1],
])

b = Matrix(list(map(lambda x: (-int(x)) % m, input().split())))

# Compute the integer determinant
det = int(A.det())

if gcd(det, m) == 1:
    # Solution formula: det(A)^(-1) * adj(A) * b (mod m)
    det_inv = pow(det, -1, m)
    x = (det_inv * A.adjugate() @ b) % m
    print("Solution Vector x:\n", x)
else:
    print("Determinant and modulus are not coprime. Use Gaussian Elimination.")
