import scipy.interpolate as sp
import numpy as np
import matplotlib.pyplot as plt

Re = [0.2, 2, 20, 200, 2000, 20000]
cd = [103, 13.9, 2.72, 0.8, 0.401, 0.433]

logRe = np.log(Re)
logCd = np.log(cd)

poly = sp.CubicSpline(logRe, logCd)

x1 = np.arange(0.2, 20000, 1)
y1 = np.exp(poly(np.log(x1)))

x2 = [5, 50, 5000]
y2 = np.exp(poly(np.log(x2)))

print(f"cp(5) = {y2[0]}, cp(50) = {y2[1]}, cp(5000) = {y2[2]}")

plt.plot(Re, cd, "o")
plt.plot(x1, y1)
plt.plot(x2, y2, "o")
plt.loglog()
plt.show()