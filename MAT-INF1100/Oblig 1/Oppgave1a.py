import math

"""
Oppgåve 1 a)
Vi skal sjå på differenslikninga
xn+2 −2xn+1 − xn = 0

Neste verdi er gitt ved
xn+2 = 2xn+1 + xn

i Oppgåve a) er x0 = 1 og x1 = 2.
"""

#startverdiar
x0 = 1
x1a = 2
x1b = (1-math.sqrt(2))

"""
Funksjon for kalkulering og utskrift av
rekkja produsert av ei differenslikning
"""
def difflik (x0, x1):
	#n-leddet vi held på å kalkulere
	n = 2

	#startvilkår
	xpp = x0
	xp = x1

	print ('x0 = %g' %(x0))
	print ('x1 = %.20f' %(x1))

	for i in range (n, 101):
		#kalkuler neste verdi i rekkja
		x = (2*xp)+xpp

		print('x%g = %2.20f' %(n, x))

		#inkrementer n verdien
		n += 1

		#gå vidare i rekkja
		xpp = xp
		xp = x



print('Oppgåve 1a)')
print('\n\nx0 = 1, x1 = 2\n')
difflik(x0, x1a)
