from scipy import optimize
import math
import numpy as np 

# x + math.e**(-x) + y**3
# x**2 + 2*x*y - y**2 + math.tan(math.radians(x))
# x**2 + y**2 - 4

def equations(z):
    x, y = z
    f = math.tan(x) - y - 1
    g = math.cos(x) - 3 * math.sin(y)
    return [f, g]

result = []
for i in np.arange(0, 1.5, 0.001):
    for j in np.arange(0, 1.5, 0.01):
        x1 = optimize.root(equations, [i, j])
        if(x1.success):
            if 0 <= round(x1.x[0], 3) <= 1.5:
                if [round(x1.x[0], 3), round(x1.x[1], 3)] not in result:
                    result.append([round(x1.x[0], 3), round(x1.x[1], 3)])

print(result)