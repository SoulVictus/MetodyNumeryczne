import numpy as np
import scipy.interpolate as sp
import matplotlib.pyplot as plt

x = np.array([0, 1.525, 3.05, 4.575, 6.1, 7.625, 9.150])
y = np.array([1, 0.8617, 0.7385, 0.6292, 0.5328, 0.4481, 0.3741])

func = np.polyfit(x, y, 2)
quadratic = np.poly1d(func)

dx = np.arange(0, 10.5, 0.01)
print(f"p(10.5) = {quadratic(10.5)}")

plt.plot(dx, quadratic(dx))
plt.plot(x, y, "o")
plt.plot(10.5, quadratic(10.5),"x")
plt.show()

# funkcja polyfit używa metody najmniejszych kwadratów

