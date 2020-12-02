import scipy.optimize as sp
import numpy as np 

def f(x):
    return 2*x**4 + 24*x**3 + 61*x**2 - 16*x + 1

result = []

result.append(sp.ridder(f, -5, 8))
result.append(sp.ridder(f, -9, -6))

print(result)

# znalazłem 2 miejsca zerowe