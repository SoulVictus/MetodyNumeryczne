import math
import numpy as np
import matplotlib.pyplot as plt
cpx1 = complex(5,1)
cpx2 = complex(8,-5)
cpx3 = complex(30,-14)

poly = [1, cpx1, -cpx2, cpx3, -84]

result = np.roots(poly)

print(result)