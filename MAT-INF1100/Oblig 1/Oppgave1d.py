import math

"""
Vi skal sjå på differenslikninga
xn+2 −2xn+1 − xn = 0

Neste verdi er gitt ved
xn+2 = 2xn+1 + xn

i Oppgåve d) er x0 = 1 og x1 = 1-sqrt(2)
"""

#startverdiar
x0 = 1
x1 = (1-math.sqrt(2))

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
	print ('x1 = %g' %(x1))

	for i in range (n, 101):
		#kalkuler neste verdi i rekkja
		x = (2*xp)+xpp
		#eksakt verdi fra generell formel
		gn = generell_løysing(n)

		#utskrift av differensverdi, eksakt verdi og avstanden mellom
		print('x%g = %g, exact = %g, difference = %g' %(n, x, gn, abs(gn - x)))

		#inkrementer n verdien
		n += 1

		#gå vidare i rekkja
		xpp = xp
		xp = x


def generell_løysing (n):

	xn = (1-math.sqrt(2))**n

	return xn

print('Oppgåve 1d)')
print('\n\nx0 = 1, x1 = 1-sqrt(2)\n')

difflik(x0, x1)

for i in range (0, 101):
	generell_løysing(i)
