"""
Plotting and visualizing functions in python

curves are visualized by drawing straight lines between points along the curve

store coordinates in lists or ARRAYS, (x, y)

arrays ~ lists , but more efficient

Vectors: point (x,y) in plane, (x,y,z) in space

vector = n-tuple of numbers

v = (v0, --- vn-1)

vi,  v[i] as lists, we will use arrays


import numpy as np

n = 5
x = np.linspace(0, 1, n)  n points in [0,1]
y = np.zeros(n)

for i in range(n):
    y[i] = f(x[i])

use arrays for sequences of numbers! float, int, complex

y = np.sin(x) , x,y : arrays
