#payback of loan a.1.6

from numpy import *
from matplotlib.pyplot import *

L = 100
p = 5
N = 360 #months

index_set = range(N+1)
x = zeros(len(index_set))
y = zeros(len(index_set))

x[0] = L
y[0] = 0

for n in index_set[1:]:
    y[n] = x[n-1]*p/(12*100) + L/N
    x[n] = x[n-1] + x[n-1]*p/(12*100) - y[n]

plot(x,'ro') #red cirles
plot(y,'b+') #blue pluses

show()
