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

# c)

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

# e)

print('\t N\tError')
epsilon_h = []
for x in range (4, 11):
	N = 2**x
	h = T/N
	epsilon_h.append((h, abs(lin_pendel_euler(v0, theta0, g, L, N, h)[1][N] \
	 - analytisk_pendel(v0, theta0, g, L, t[-1]))))

	print ('\t2**%g\t%g' %(x, epsilon_h[x-4][1]))

# f)

print('\t N\t Error \t\t    p')
orden_p = []
for j in range(6):
    N  = 2**(j+4)
    h1 = epsilon_h[j][0]
    h2 = epsilon_h[j+1][0]
    
    e_h1 = epsilon_h[j][1]
    e_h2 = epsilon_h[j+1][1]
    
    orden_p.append(np.log(e_h1/e_h2)/np.log(h1/h2))
    
    print ('\t2**%g\t %g \t %g' %(j+4, abs(epsilon_h[j][1]), orden_p[j]))



# d)
plt.plot(np.linspace(0,4,2**5+1), theta_n2_5, label = 'Euler n = 2**5')
plt.plot(np.linspace(0,4,2**10+1), theta_n2_10, label = 'Euler n = 2**10')
plt.plot(t, theta, label = 'Analytisk resultat')
plt.xlabel('tid')
plt.ylabel('vinkelutslaget')
plt.xlim(0,4)
plt.legend()

plt.grid()
plt.show()






"""
Terminal> python Oppgave_2.py
     N      Error
    2**4    27.3939
    2**5    10.9065
    2**6    3.56439
    2**7    1.31314
    2**8    0.561413
    2**9    0.259755
    2**10   0.12498
     N       Error              p
    2**4     27.3939         1.32867
    2**5     10.9065         1.61346
    2**6     3.56439         1.44064
    2**7     1.31314         1.22588
    2**8     0.561413        1.11191
    2**9     0.259755        1.05546

Programmet teiknar tre figurar i same vindu.

"""