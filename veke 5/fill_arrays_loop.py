"""
From the excercise book:
Exercise 5.1. Fill arrays; loop version

We study the function
f(x) = ln(x).
We want to fill two arrays x and y with x and f(x) values, respectively. Use 101
uniformly spaced x values in the interval [1, 10]. Create empty x and y arrays
and compute each element in x and y with a for loop.
"""

import numpy as np

# function that returns ln(x)
def f(x):
	return np.log(x)

N = 100
index_set = range(N+1)


x = np.zeros(len(index_set))
y = np.zeros(len(index_set))

#create evenly spaced elements in x, calculate y values for each x
dN = (10-1)/N
for i in index_set:
	x[i] = 1+i*dN
	y[i] = f(x[i])

#print to observe values
for a,b in zip (x,y):
	print ('x=%5.2f, y=%.4f' %(a,b))

"""
TERMINAL> python fill_arrays_loop.py
x= 1.00, y=0.0000
x= 1.09, y=0.0862
x= 1.18, y=0.1655
x= 1.27, y=0.2390
x= 1.36, y=0.3075
x= 1.45, y=0.3716
x= 1.54, y=0.4318
x= 1.63, y=0.4886
x= 1.72, y=0.5423
x= 1.81, y=0.5933
x= 1.90, y=0.6419
x= 1.99, y=0.6881
x= 2.08, y=0.7324
x= 2.17, y=0.7747
x= 2.26, y=0.8154
x= 2.35, y=0.8544
x= 2.44, y=0.8920
x= 2.53, y=0.9282
x= 2.62, y=0.9632
x= 2.71, y=0.9969
x= 2.80, y=1.0296
x= 2.89, y=1.0613
x= 2.98, y=1.0919
x= 3.07, y=1.1217
x= 3.16, y=1.1506
x= 3.25, y=1.1787
x= 3.34, y=1.2060
x= 3.43, y=1.2326
x= 3.52, y=1.2585
x= 3.61, y=1.2837
x= 3.70, y=1.3083
x= 3.79, y=1.3324
x= 3.88, y=1.3558
x= 3.97, y=1.3788
x= 4.06, y=1.4012
x= 4.15, y=1.4231
x= 4.24, y=1.4446
x= 4.33, y=1.4656
x= 4.42, y=1.4861
x= 4.51, y=1.5063
x= 4.60, y=1.5261
x= 4.69, y=1.5454
x= 4.78, y=1.5644
x= 4.87, y=1.5831
x= 4.96, y=1.6014
x= 5.05, y=1.6194
x= 5.14, y=1.6371
x= 5.23, y=1.6544
x= 5.32, y=1.6715
x= 5.41, y=1.6882
x= 5.50, y=1.7047
x= 5.59, y=1.7210
x= 5.68, y=1.7370
x= 5.77, y=1.7527
x= 5.86, y=1.7681
x= 5.95, y=1.7834
x= 6.04, y=1.7984
x= 6.13, y=1.8132
x= 6.22, y=1.8278
x= 6.31, y=1.8421
x= 6.40, y=1.8563
x= 6.49, y=1.8703
x= 6.58, y=1.8840
x= 6.67, y=1.8976
x= 6.76, y=1.9110
x= 6.85, y=1.9242
x= 6.94, y=1.9373
x= 7.03, y=1.9502
x= 7.12, y=1.9629
x= 7.21, y=1.9755
x= 7.30, y=1.9879
x= 7.39, y=2.0001
x= 7.48, y=2.0122
x= 7.57, y=2.0242
x= 7.66, y=2.0360
x= 7.75, y=2.0477
x= 7.84, y=2.0592
x= 7.93, y=2.0707
x= 8.02, y=2.0819
x= 8.11, y=2.0931
x= 8.20, y=2.1041
x= 8.29, y=2.1150
x= 8.38, y=2.1258
x= 8.47, y=2.1365
x= 8.56, y=2.1471
x= 8.65, y=2.1576
x= 8.74, y=2.1679
x= 8.83, y=2.1782
x= 8.92, y=2.1883
x= 9.01, y=2.1983
x= 9.10, y=2.2083
x= 9.19, y=2.2181
x= 9.28, y=2.2279
x= 9.37, y=2.2375
x= 9.46, y=2.2471
x= 9.55, y=2.2565
x= 9.64, y=2.2659
x= 9.73, y=2.2752
x= 9.82, y=2.2844
x= 9.91, y=2.2935
x=10.00, y=2.3026
"""