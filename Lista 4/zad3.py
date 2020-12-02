import numpy as np

def velocity(t):
    u = 2510
    Mo = 2.8 * 10**6
    m = 13.3 * 10**3
    g = 9.81
    return u * np.log(Mo/(Mo - m*t)) - g*t

time = np.linspace(1, 100, 100000)

for ti in time:
    if(velocity(ti) >= 335):
        print(f"Velocity: {velocity(ti)} Time: {ti}")
        break
    

