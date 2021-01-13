import matplotlib.pyplot as plt
import scipy.misc as sp
import numpy as np

def f(x):
    return np.log(np.tanh(x/(x**2 + 1)))

dx1 = sp.derivative(f, 0.2, 0.00001)
dx2 = sp.derivative(f, 0.2, 0.00001, 2)
dx3 = sp.derivative(f, 0.2, 0.0001, 3, order=5)

print(f"dx1 = {dx1}, dx2 = {dx2}, dx3 = {dx3}")