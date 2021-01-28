from scipy.linalg import eigh_tridiagonal
import numpy as np

diagonal1 = 2 * np.ones(10)
off_diagonal1 = -1 * np.ones(9)

diagonal2 = 2 * np.ones(100)
off_diagonal2 = -1 * np.ones(99)

w1, v1 = eigh_tridiagonal(diagonal1, off_diagonal1)
w2, v2 = eigh_tridiagonal(diagonal2, off_diagonal2)

print("Wartości własne macierzy 10x10: ", w1[:3], sep="\n")
print("Wektory własne macierzy 10x10: ", v1[:, :3], sep="\n")
print("\n")
print("Wartości własne macierzy 100x100: ", w2[:3], sep="\n")
print("Wektory własne macierzy 100x100: ", v2[:, :3], sep="\n")