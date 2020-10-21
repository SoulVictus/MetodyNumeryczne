import math

for i in range(2, 26, 2):
    x = 2**(-i)
    result = math.sqrt(x**4 + 4) - 2
    print("{0}. {1}".format(i, result))

print("\n")

for i in range(2, 26, 2):
    x = 2**(-i)
    result = x**4/(math.sqrt(x**4 + 4) + 2)
    print("{0}. {1}".format(i, result))


# Widać, że drugi sposób jest dużo bardziej dokładny