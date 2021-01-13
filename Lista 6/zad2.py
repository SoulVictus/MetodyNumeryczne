import scipy.interpolate as sp
import numpy as np 

x = [0.0, 0.1, 0.2, 0.3, 0.4]
y = [0.0, 0.078348, 0.13891, 0.192916, 0.244981]

poly = sp.lagrange(x, y)

poly_der = np.polyder(poly)

print(f"f'(0.2) = {poly_der(0.2)}")