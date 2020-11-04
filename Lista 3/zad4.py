import numpy as np
import sys

def gauss_elimination(matrix):
    a = matrix
    n = len(a)
    x = np.zeros(n)

    for i in range(n):
        if a[i][i] == 0.0:
            sys.exit('Divide by zero detected!')

        for j in range(i+1, n):
            ratio = a[j][i]/a[i][i]

            for k in range(n+1):
                a[j][k] = a[j][k] - ratio * a[i][k]

    x[n-1] = a[n-1][n]/a[n-1][n-1]

    for i in range(n-2,-1,-1):
        x[i] = a[i][n]

        for j in range(i+1,n):
            x[i] = x[i] - a[i][j]*x[j]

        x[i] = x[i]/a[i][i]

    for i in range(n):
        print('X%d = %0.2f' %(i,x[i]), end = '\n')


#zad 1
#x1 = np.array([[-1,1,-4,0], [2,2,0,1], [3,3,2,1/2]])
#gauss_elimination(x1)

#zad 2 
#z = np.array([[1, 0, 0, 1], [3/2, 1, 0, -1], [1/2, 11/13, 1, 2]])
#gauss_elimination(z)
#x = np.array([[2,-3,-1,1], [0, 13/2, -7/2, -5/2], [0,0, 32/13, 94/26]])
#gauss_elimination(x)

#zad 3
#a = np.array([[0, 0, 2, 1, 2, 1], [0, 1, 0, 2, -1, 1], [1, 2, 0, -2, 0, -4], [0, 0, 0, -1, 1, -2], [0, 1, -1, 1, -1, -1]],dtype=float)
#gauss_elimination(a)