import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as sp

x = [1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3]
y = [-0.5403, -0.0104, 0.9423, 1.7445, 1.3073, -0.7718, -2.4986, -0.7903, 2.7334]

poly = sp.CubicSpline(x, y)
poly_deriv = poly.derivative()
print(f"y'(2.1) = {poly_deriv(2.1)}")

x_list = np.linspace(1, 3, 100)
plt.plot(x_list, poly(x_list))

z = np.polyfit(x, y, 7)
p = np.poly1d(z)
pp = p.deriv()
ppp = pp.deriv()

x_roots = poly.roots()
y_roots = np.zeros(len(x_roots))

print(x_roots)

plt.plot(x_roots, y_roots, "or")
plt.grid()
plt.xlim(1, 3)
plt.show()
