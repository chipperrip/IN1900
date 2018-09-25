#funksjon som reiknar ut binomialkoeffisientar
def binkof (n, i):
    nCr = 1
    for j in range (1, n-i+1):
        nCr *= (i+j)/j

    print ('n = %6.0f  i = %3.0f  binomialkoeffisient:' %(n, i), nCr)

binkof(5000,4)
binkof(100000,60)
binkof(1000,500)
