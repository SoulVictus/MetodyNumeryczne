from scipy import optimize
import numpy as np 
import math

h = 2 # wysokość rzutu piłki 
d = 10 # odległość od kosza
l = 3 # wysokość kosza
g = 9.81 # przyciąganie grawitacyjne
ang = 45 # kąt wpadania 

def func(data):
    v0, angle = data
    t = 10 / (v0 * np.cos(angle))
    f1 = v0 * np.sin(angle) * t - ((g * t**2)/2) - 1
    f2 = v0 * (np.sin(angle) + np.cos(angle)) - (g*t)
    return[f1,f2]


result = optimize.fsolve(func,[10.4,math.radians(50)])
print("V0: ", result[0])
print("alpha: ", math.degrees(result[1]))