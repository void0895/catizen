import numpy as np

rows = 2
cols = 2
x = np.arange(rows * cols).reshape(rows, cols)
print("first matrix", x)
y = np.arange(rows * cols).reshape(rows, cols)
print("second matrix", y)

for i in range(len(x)):
    for j in range(len(x[0])):
        xz = x[i][j] + y[i][j]
        print(xz)
