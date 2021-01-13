import numpy as np
import scipy.special as sp

def  f(x):
    return (np.log(x)/(x**2-2*x+2))

a = 1
b = np.pi
w = [2, 4]

for n in w:
    x, wi, mu = sp.roots_legendre(n, mu = True)
    result = 0
    for i in range(len(x)):
        result += (b - a)/2 * f((b + a)/2 + (b - a)/2 * x[i])*wi[i]
    print(f"Intervals: {n}, result = {result}")