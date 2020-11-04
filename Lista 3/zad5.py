import numpy as np
from scipy import linalg

for n in range(5, 21, 5):
    if n != 15:
        hilb = linalg.hilbert(n)
        norm = linalg.norm(hilb)
        cond = np.linalg.cond(hilb)
        print(f"Norm of {n}:\n{norm}\nCondition Number:\n{cond}\n")

