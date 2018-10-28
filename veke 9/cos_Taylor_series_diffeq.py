"""
Frå boka:

Exercise A.15: Find difference equations for computing cos x
"""

import numpy as np
import matplotlib.pyplot as plt

def cos_Taylor(x, n):

	s = np.zeros(n+2)
	a = np.zeros(n+2)

	s[0] = 0
	a[0] = 1

	for j in range(1, n+2):

		s[j] = s[j-1] + a[j-1]
		a[j] = (-1) * ((x**2) / ((2*j)*((2*j)-1))) * a[j-1]

	return s[n+1], abs(a[n+1])

# same framgangsmåte som på forelesning 2. okt:
def cos_two_terms(x):
	s = np.zeros(4)
	a = np.zeros(4)

	s[0] = 0
	a[0] = 1
	s[1] = s[0] + a[0]
	a[1] = (-1) * ((x**2) / ((2*1)*((2*1)-1))) * a[0]
	s[2] = s[1] + a[1]
	a[2] = (-1) * ((x**2) / ((2*2)*((2*2)-1))) * a[1]
	s[3] = s[2] + a[2]
	a[3] = (-1) * ((x**2) / ((2*3)*((2*3)-1))) * a[2]
	return s[3], abs(a[3])

# basert på forelesning 2. okt:
def test_cos_Taylor():
	x = 0.63 # Just an arbitrary x-value for validation
	tol = 1e-14 # Tolerance
	s_expected, a_expected = cos_two_terms(x)
	s_computed, a_computed = cos_Taylor(x,2)
	success1 = abs(s_computed - s_expected) < tol
	success2 = abs(a_computed - a_expected) < tol
	success = success1 and success2
	message = 'Output is different from expected!'
	assert success, message

test_cos_Taylor()






"""
Terminal python cos_Taylor_series_diffeq.py

Ingen feilmelding frå testen.

Var seint ute med oppgåva og fekk ikkje tid til å plotte.


"""