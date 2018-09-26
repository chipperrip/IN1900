from random import random

antfeil = 0; N = 100000

for i in range(N):
    x = random(); y = random(); z = random();

    res1 = (x*y)*z
    res2 = x*(y*z)

    if res1 != res2:
        antfeil += 1
        x0 = x; y0 = y; z0 = z
        ikkeass1 = res1
        ikkeass2 = res2

print (100. * antfeil/N)
print (x0, y0, z0, ikkeass1 - ikkeass2)
