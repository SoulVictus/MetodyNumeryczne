import scipy.integrate as sp
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.cos(2*np.cos(x)**-1)

for n in [3,5,7]:
    x = np.linspace(-1, 1, n)
    fx = []
    for xx in x:
        fx.append(f(xx))
    result = sp.simps(fx, x)
    print(result)