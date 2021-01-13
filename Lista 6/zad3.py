import scipy.interpolate as sp
import numpy as np 

x = [-2.2, -0.3, 0.8, 1.9]
y = [-15.18, 10.962, 1.92, -2.04]

poly = sp.lagrange(x, y)

poly_der = np.polyder(poly)
poly_der2 = np.polyder(poly, 2)

print(f"f'(0) = {poly_der(0)}, f``(0) = {poly_der2(0)}")