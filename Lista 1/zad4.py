import numpy as np



def hilbert_matrix(n):
    arr = []
    for i in range(0,n):
        row = []
        for j in range(0, n):
            el = 1/(i + j + 1)
            row.append(el)
        arr.append(row)
    return np.array(arr)

nparr1 = hilbert_matrix(4)
print("######## ARRAY 1 #########")
print(nparr1)
print("######## ARRAY 1 INVERSION #########")
print(np.linalg.inv(nparr1))
print("\n")

nparr2 = hilbert_matrix(8)
print("######## ARRAY 2 #########")
print(nparr2)
print("######## ARRAY 2 INVERSION #########")
print(np.linalg.inv(nparr2))
print("\n")

for x in range(5, 21):
    print("Determinant of matrix {0}x{1}".format(x, x))
    print(np.linalg.det(hilbert_matrix(x)))
