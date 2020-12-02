import scipy.optimize as sp
import numpy as np

f = lambda x, a: x**5 - a
fder = lambda x, a: 5*x**4
x = np.random.randn(10)
a = np.arange(1, 11)

vec_res = sp.newton(f, x, fprime = fder, args=(a, ))

print(vec_res)