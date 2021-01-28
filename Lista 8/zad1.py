import scipy.linalg as sp
import numpy as np

A = np.array([[-1, -4, 1],
[-1, -2, -5],
[5, 4, 3]])

w, v = sp.eig(A)

print("Wartości własna: ", w)
print("Wektory własne: ", v)