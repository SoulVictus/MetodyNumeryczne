import numpy as np
import scipy.interpolate as sp

A = np.array([0, 3, 6])

B = np.array([1.225, 0.905, 0.652])
x = sp.lagrange(A, B)

print(x)
