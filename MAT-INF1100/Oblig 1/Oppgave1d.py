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

	print ('x  0 = %g' %(x0))
	print ('x  1 = %g' %(x1))

	for i in range (n, 101):
		#kalkuler neste verdi i rekkja
		x = (2*xp)+xpp
		#eksakt verdi fra generell formel
		gn = generell_løysing(n)

		#utskrift av differensverdi, eksakt verdi og avstanden mellom
		print('x%3.0f = %g, exact = %g, difference = %g' %(n, x, gn, abs(gn - x)))

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

"""
TERMINAL> python Oppgave1d.py
Oppgåve 1d)


x0 = 1, x1 = 1-sqrt(2)

x  0 = 1
x  1 = -0.414214
x  2 = 0.171573, exact = 0.171573, difference = 2.77556e-16
x  3 = -0.0710678, exact = -0.0710678, difference = 4.30211e-16
x  4 = 0.0294373, exact = 0.0294373, difference = 1.18655e-15
x  5 = -0.0121933, exact = -0.0121933, difference = 2.78944e-15
x  6 = 0.00505063, exact = 0.00505063, difference = 6.7741e-15
x  7 = -0.00209204, exact = -0.00209204, difference = 1.63342e-14
x  8 = 0.000866552, exact = 0.000866552, difference = 3.94441e-14
x  9 = -0.000358937, exact = -0.000358937, difference = 9.52221e-14
x 10 = 0.000148677, exact = 0.000148677, difference = 2.29889e-13
x 11 = -6.15839e-05, exact = -6.15839e-05, difference = 5.54999e-13
x 12 = 2.55089e-05, exact = 2.55089e-05, difference = 1.33989e-12
x 13 = -1.05661e-05, exact = -1.05661e-05, difference = 3.23477e-12
x 14 = 4.37663e-06, exact = 4.37664e-06, difference = 7.80943e-12
x 15 = -1.81288e-06, exact = -1.81286e-06, difference = 1.88536e-11
x 16 = 7.50866e-07, exact = 7.50912e-07, difference = 4.55167e-11
x 17 = -3.11148e-07, exact = -3.11038e-07, difference = 1.09887e-10
x 18 = 1.28571e-07, exact = 1.28836e-07, difference = 2.65291e-10
x 19 = -5.40061e-08, exact = -5.33657e-08, difference = 6.40469e-10
x 20 = 2.05586e-08, exact = 2.21048e-08, difference = 1.54623e-09
x 21 = -1.2889e-08, exact = -9.1561e-09, difference = 3.73293e-09
x 22 = -5.2195e-09, exact = 3.79258e-09, difference = 9.01208e-09
x 23 = -2.3328e-08, exact = -1.57094e-09, difference = 2.17571e-08
x 24 = -5.18755e-08, exact = 6.50704e-10, difference = 5.25262e-08
x 25 = -1.27079e-07, exact = -2.6953e-10, difference = 1.2681e-07
x 26 = -3.06034e-07, exact = 1.11643e-10, difference = 3.06145e-07
x 27 = -7.39147e-07, exact = -4.62441e-11, difference = 7.391e-07
x 28 = -1.78433e-06, exact = 1.91549e-11, difference = 1.78435e-06
x 29 = -4.3078e-06, exact = -7.93424e-12, difference = 4.30779e-06
x 30 = -1.03999e-05, exact = 3.28647e-12, difference = 1.03999e-05
x 31 = -2.51077e-05, exact = -1.3613e-12, difference = 2.51077e-05
x 32 = -6.06152e-05, exact = 5.63869e-13, difference = 6.06152e-05
x 33 = -0.000146338, exact = -2.33562e-13, difference = 0.000146338
x 34 = -0.000353292, exact = 9.67446e-14, difference = 0.000353292
x 35 = -0.000852921, exact = -4.00729e-14, difference = 0.000852921
x 36 = -0.00205913, exact = 1.65987e-14, difference = 0.00205913
x 37 = -0.00497119, exact = -6.87543e-15, difference = 0.00497119
x 38 = -0.0120015, exact = 2.84789e-15, difference = 0.0120015
x 39 = -0.0289742, exact = -1.17964e-15, difference = 0.0289742
x 40 = -0.0699499, exact = 4.88622e-16, difference = 0.0699499
x 41 = -0.168874, exact = -2.02394e-16, difference = 0.168874
x 42 = -0.407698, exact = 8.38342e-17, difference = 0.407698
x 43 = -0.98427, exact = -3.47253e-17, difference = 0.98427
x 44 = -2.37624, exact = 1.43837e-17, difference = 2.37624
x 45 = -5.73675, exact = -5.95791e-18, difference = 5.73675
x 46 = -13.8497, exact = 2.46785e-18, difference = 13.8497
x 47 = -33.4362, exact = -1.02222e-18, difference = 33.4362
x 48 = -80.7222, exact = 4.23416e-19, difference = 80.7222
x 49 = -194.881, exact = -1.75385e-19, difference = 194.881
x 50 = -470.483, exact = 7.26467e-20, difference = 470.483
x 51 = -1135.85, exact = -3.00912e-20, difference = 1135.85
x 52 = -2742.18, exact = 1.24642e-20, difference = 2742.18
x 53 = -6620.2, exact = -5.16284e-21, difference = 6620.2
x 54 = -15982.6, exact = 2.13852e-21, difference = 15982.6
x 55 = -38585.4, exact = -8.85803e-22, difference = 38585.4
x 56 = -93153.3, exact = 3.66912e-22, difference = 93153.3
x 57 = -224892, exact = -1.5198e-22, difference = 224892
x 58 = -542937, exact = 6.29521e-23, difference = 542937
x 59 = -1.31077e+06, exact = -2.60756e-23, difference = 1.31077e+06
x 60 = -3.16447e+06, exact = 1.08009e-23, difference = 3.16447e+06
x 61 = -7.63971e+06, exact = -4.47387e-24, difference = 7.63971e+06
x 62 = -1.84439e+07, exact = 1.85314e-24, difference = 1.84439e+07
x 63 = -4.45275e+07, exact = -7.67594e-25, difference = 4.45275e+07
x 64 = -1.07499e+08, exact = 3.17948e-25, difference = 1.07499e+08
x 65 = -2.59525e+08, exact = -1.31698e-25, difference = 2.59525e+08
x 66 = -6.26549e+08, exact = 5.45513e-26, difference = 6.26549e+08
x 67 = -1.51262e+09, exact = -2.25959e-26, difference = 1.51262e+09
x 68 = -3.6518e+09, exact = 9.35952e-27, difference = 3.6518e+09
x 69 = -8.81622e+09, exact = -3.87684e-27, difference = 8.81622e+09
x 70 = -2.12842e+10, exact = 1.60584e-27, difference = 2.12842e+10
x 71 = -5.13847e+10, exact = -6.6516e-28, difference = 5.13847e+10
x 72 = -1.24054e+11, exact = 2.75518e-28, difference = 1.24054e+11
x 73 = -2.99492e+11, exact = -1.14123e-28, difference = 2.99492e+11
x 74 = -7.23037e+11, exact = 4.72715e-29, difference = 7.23037e+11
x 75 = -1.74557e+12, exact = -1.95805e-29, difference = 1.74557e+12
x 76 = -4.21417e+12, exact = 8.11051e-30, difference = 4.21417e+12
x 77 = -1.01739e+13, exact = -3.35948e-30, difference = 1.01739e+13
x 78 = -2.4562e+13, exact = 1.39154e-30, difference = 2.4562e+13
x 79 = -5.92979e+13, exact = -5.76396e-31, difference = 5.92979e+13
x 80 = -1.43158e+14, exact = 2.38751e-31, difference = 1.43158e+14
x 81 = -3.45613e+14, exact = -9.88939e-32, difference = 3.45613e+14
x 82 = -8.34384e+14, exact = 4.09632e-32, difference = 8.34384e+14
x 83 = -2.01438e+15, exact = -1.69675e-32, difference = 2.01438e+15
x 84 = -4.86315e+15, exact = 7.02817e-33, difference = 4.86315e+15
x 85 = -1.17407e+16, exact = -2.91116e-33, difference = 1.17407e+16
x 86 = -2.83445e+16, exact = 1.20584e-33, difference = 2.83445e+16
x 87 = -6.84297e+16, exact = -4.99477e-34, difference = 6.84297e+16
x 88 = -1.65204e+17, exact = 2.0689e-34, difference = 1.65204e+17
x 89 = -3.98837e+17, exact = -8.56967e-35, difference = 3.98837e+17
x 90 = -9.62879e+17, exact = 3.54967e-35, difference = 9.62879e+17
x 91 = -2.32459e+18, exact = -1.47032e-35, difference = 2.32459e+18
x 92 = -5.61207e+18, exact = 6.09028e-36, difference = 5.61207e+18
x 93 = -1.35487e+19, exact = -2.52267e-36, difference = 1.35487e+19
x 94 = -3.27095e+19, exact = 1.04493e-36, difference = 3.27095e+19
x 95 = -7.89678e+19, exact = -4.32823e-37, difference = 7.89678e+19
x 96 = -1.90645e+20, exact = 1.79281e-37, difference = 1.90645e+20
x 97 = -4.60258e+20, exact = -7.42606e-38, difference = 4.60258e+20
x 98 = -1.11116e+21, exact = 3.07598e-38, difference = 1.11116e+21
x 99 = -2.68258e+21, exact = -1.27411e-38, difference = 2.68258e+21
x100 = -6.47632e+21, exact = 5.27754e-39, difference = 6.47632e+21
"""