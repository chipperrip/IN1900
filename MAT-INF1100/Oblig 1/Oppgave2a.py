#funksjon som reiknar ut binomialkoeffisientar
def binkof (n, i):
    nCi = 1
    for j in range (1, n-i+1):
        nCi *= (i+j)/j

    print ('n = %6.0f  i = %3.0f  binomialkoeffisient: ' %(n, i), nCi)

binkof(5000,4)
binkof(100000,60)
binkof(1000,500)

"""
TERMINAL> python Oppgave2a.py
n =   5000  i =   4  binomialkoeffisient:  26010428123750.86
n = 100000  i =  60  binomialkoeffisient:  1.1806919799625589e+218
n =   1000  i = 500  binomialkoeffisient:  2.7028824094543663e+299
"""