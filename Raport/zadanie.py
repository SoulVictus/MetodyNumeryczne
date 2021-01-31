import scipy.integrate as sp
from scipy.signal import argrelextrema
import numpy as np
import matplotlib.pyplot as plt

def f(t, y):
  return [y[1], -3*y[1] + 10*y[0]]

t0 = 0 # t początkowe.
tk = 1 # t końcowe.
t = np.linspace(t0, tk, 1000)

yp = 4 # warunek początkowy y(0) = 4.
ydp = -2 # warunek początkowy y'(0) = -2.
y0 = [yp, ydp]

result = sp.solve_ivp(f, [t0, tk], y0, t_eval=t, method="BDF")

# Narysowanie rozwiązania równania różniczkowego.
plt.plot(result.t, result.y[0])

# Wypisywanie punktów:

# points = dict(zip(result.y[0], t))
# indx = 1
# for result, point in points.items():
#   print(f"{indx}. t = {point}, result = {result}")
#   indx = indx + 1

extremum = argrelextrema(result.y[0], np.less)[0]
print(f"Ekstremum występuje między:\nt = {result.t[extremum]} i t = {result.t[extremum+1]}\n t[47] = {result.y[0][47]} i t[48] = {result.y[0][48]}.")

# Narysowanie pochodnej naszego rozwiązania.
plt.plot(result.t, result.y[1])

# Opisanie wykresu
plt.legend(["y", "dy/dt"])
plt.xlabel("t values")
plt.ylabel("y values")
plt.title("Równanie różniczkowe drugiego rzędu metodą BDF. y\'\' + 3y\' - 10y = 0")

# Narysowanie punktu y(0) = 4.
plt.plot(t0, yp, "go")
# Narysowanie punktu y'(0) = -2.
plt.plot(t0, ydp,"go")
# Narysowanie ekstremum
plt.plot(result.t[extremum], result.y[0][47], "bo")
plt.grid()
plt.show()