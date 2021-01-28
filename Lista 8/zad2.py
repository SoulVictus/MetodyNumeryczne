import scipy.linalg as sp
import numpy as np

A = sp.hilbert(6)

w, v = sp.eig(A)

print("Wartości własna: ", w)
print("Wektory własne: ", v)