import numpy as np
import scipy.interpolate as sp
import matplotlib.pyplot as plt

x = [1.0, 1.1, 1.8, 2.2, 2.5, 3.5, 3.7, 4.0]
y = [6.008, 5.257, 9.549, 11.098, 15.722, 27.13, 28.828, 33.772]

dx = np.arange(1, 4, 0.01)

lineal_func = np.polyfit(x, y, 1)
lineal = np.poly1d(lineal_func)

quadratic_func = np.polyfit(x, y, 2)
quadratic = np.poly1d(quadratic_func)

plt.plot(x, y, "o")
plt.plot(dx, lineal(dx))
plt.plot(dx, quadratic(dx))
plt.show()

# funkcja kwadratowa jest lepiej dopasowana do tych danych