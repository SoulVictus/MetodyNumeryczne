import numpy as np
import scipy.integrate as sp


def f(alpha,zero):
    return 1/np.sqrt(1-np.sin(np.deg2rad(zero/2))**2 * np.sin(np.deg2rad(alpha))**2)

def f2(h):
    return 4*np.sqrt(1/9.81)*h

x = np.arange(0, np.pi/2, 0.01)
fx = []

for step in x:
    fx.append(f(x, 15))

integral = sp.simps(fx, x)

print(f2(integral[0]))

fx.clear()
for step in x:
    fx.append(f(x, 30))
integral = sp.simps(fx, x)

print(f2(integral[0]))

fx.clear()
for step in x:
    fx.append(f(x, 45))
integral = sp.simps(fx, x)

print(f2(integral[0]))