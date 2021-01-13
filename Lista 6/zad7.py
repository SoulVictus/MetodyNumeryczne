import scipy.integrate as sp
import numpy as np

def f(x):
    return (np.cos(x) - np.exp(x))/np.sin(x)

integral1 = sp.quadrature(f, -1, 0)
integral2 = sp.quadrature(f, 0, 1)

result = integral1[0] + integral2[0]
error = integral1[1] + integral2[1]

print(f"result = {result}, error = {error}")