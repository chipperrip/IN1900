"""
MAT-INF 1100
Oblig 2
Hausten 2018

Christopher Pavelich
"""

"""
Oppgåve 2
"""
import numpy as np
import matplotlib.pyplot as plt

def lin_pendel_euler(v0, theta0, g, L, N, h):

	v = []
	v.append(v0)
	theta = []
	theta.append(theta0)

	for k in range (1,N+1):
		v.append(v[k-1] - (g*h*theta[k-1]))
		theta.append(theta[k-1] + (h*(v[k-1]/L)))
	return v, theta


def analytisk_pendel(v0, theta0, g, L, t):
    theta_t = (theta0*np.cos(np.sqrt(g/L)*t)) + ((v0/g)*np.sqrt(g/L)*np.sin(np.sqrt(g/L)*t))
    return theta_t

g = 9.81
L = 1
v0 = 0
theta0 = np.pi/2
T = 4


N = 2**5
h = T/N
v_n2_5, theta_n2_5 = lin_pendel_euler(v0, theta0, g, L, N, h)


N = 2**10
h = T/N
v_n2_5, theta_n2_10 = lin_pendel_euler(v0, theta0, g, L, N, h)

t = np.linspace(0,4,1001)
theta = analytisk_pendel(v0, theta0, g, L, t)

print('\t N\tError')
for x in range (4, 11):
	N = 2**x
	h = T/N
	print ('\t2**%g\t%g' %(x, abs(lin_pendel_euler(v0, theta0, g, L, N, h)[-1][N] \
	 - analytisk_pendel(v0, theta0, g, L, N))))

plt.plot(np.linspace(0,4,2**5+1), theta_n2_5, label = 'Euler n = 2**5')
plt.plot(np.linspace(0,4,2**10+1), theta_n2_10, label = 'Euler n = 2**10')
plt.plot(t, theta, label = 'Analytisk resultat')
plt.xlabel('tid')
plt.xlabel('vinkelutslaget')
plt.xlim(0,4)
plt.legend()

plt.grid()
plt.show()






"""
Terminal> python Oppgave_2.py
     N      Error
    2**4    27.3769
    2**5    10.9774
    2**6    3.84479
    2**7    2.33724
    2**8    3.32291
    2**9    1.59162
    2**10   3.19344

Programmet teiknar tre figurar i same vindu.

"""