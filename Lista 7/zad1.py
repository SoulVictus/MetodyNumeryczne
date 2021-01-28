import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

# function that returns dy/dt
def model(y,t):
    dydt = math.sin(t * y)
    return dydt

# initial condition
y0 = 2
y01 = 2.5
y02 = 3
y03 = 3.5


# time points
t = np.linspace(0, 6)

# solve ODE
y = odeint(model, y0, t)
y2 = odeint(model, y01, t)
y3 = odeint(model, y02, t)
y4 = odeint(model, y03, t)

# plot results
plt.plot(t, y, "o", t, y2, "o")
plt.plot(t, y3, "o", t, y4, "o")
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show()

#źródło https://apmonitor.com/pdc/index.php/Main/SolveDifferentialEquations