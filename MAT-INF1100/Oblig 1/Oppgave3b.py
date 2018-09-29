from random import random

antfeil = 0; N = 100000

for i in range(N):
    x = random(); y = random(); z = random();

    res1 = x*(y+z)
    res2 = x*y + x*z

    if res1 != res2:
        antfeil += 1
        x0 = x; y0 = y; z0 = z
        ikkeass1 = res1
        ikkeass2 = res2

print (100. * antfeil/N)
print (x0, y0, z0, ikkeass1 - ikkeass2)

"""
TERMINAL> python Oppgave3b.py
31.044
0.8458117545490976 0.9426991435326402 0.8341727472841748 -2.220446049250313e-16
"""