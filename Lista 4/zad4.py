from scipy import optimize
import numpy as np

def f(x):
    return [x[0] + np.exp(-1*x[0]) + x[1]**3, x[0]**2 + 2*x[0]*x[1] - x[1]**2 + np.tan(x[0])]


xy=[np.array([-1.270,-1.260]),np.array([-0.720,-0.700]),np.array([1.200, 1.210])]
ans=[]
for i in xy:
    x1 = optimize.root(f,i)
    if(x1.success):
        if(x1.x[0]**2 + x1.x[1]**2 <=4):
            ans.append(x1.x)
print(ans)