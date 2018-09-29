import numpy as np
import matplotlib.pyplot as plt

#a)
def seq_a(N):
    index_set = range(0,N+1,2)
    a = np.zeros(len(index_set))

    for i in range(len(a)):
        n = index_set[i]
        a[i] = (7+1.0/(n+1))/(3-1.0/((n+1)**2))

    return a

print(seq_a(100))
print(7/3)

#b)

def seq_b(N):
    index_set = range(N+1)
    d = np.zeros(len(index_set))

    for n in index_set:
        h = 2**(-n)
        d[n] = np.sin(h)/h

    return d

print(seq_b(50))

#c)

def D(f,x,N):
    index_set = range(N+1)
    d = np.zeros(len(index_set))

    for n in index_set:
        h = 2**(-n)
        d[n] =(f(x+h)-f(x))/h

    return d

#d1 = D(np.sin,0,80)
d1 = D(np.sin,np.pi,80)


plt.plot(d1, 'o',fillstyle='none')
plt.show()
