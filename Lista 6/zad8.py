import numpy as np
import scipy.integrate as sp

def f(y, x):
    return np.sin(np.pi*x)*np.sin(np.pi*(y-x))

integral = sp.dblquad(f, 0, 1, lambda x: 0, lambda x: x)

print(integral)