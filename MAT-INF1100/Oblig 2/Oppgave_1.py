"""
MAT-INF 1100
Oblig 2
Hausten 2018

Christopher Pavelich
"""

"""
Oppgåve 1
"""

import matplotlib.pyplot as plt

t = []
#v(t)
v = []

#hentar verdiane for t og v(t) frå fil
infile = open('running.txt','r')
for line in infile:
    tnext, vnext = line.strip().split(',')
    t.append(float(tnext))
    v.append(float(vnext))
infile.close()

N = len(t) - 1

#a(t)
a = []

#deriverer for å finne verdiane for a(t) frå t_0 til t_n-1
for i in range(N):
    delta_t = t[i+1]-t[i]
    delta_v = v[i+1]-v[i]
    a.append(delta_v/delta_t)

#tar med baklengs deriverte av endepunktet i t_n
a.append( (v[N]-v[N-1])/(t[N]-t[N-1]) )


s = []
#gitt verdi for s_0
s.append(0)
for j in range (1,N+1):
    #nullstill summen mellom utreikning av areala ved gitt t
	sum = 0
	#vi finn trappesummane ved midpunktmetoden
	for i in range (1,j+1):
		sum += (v[i-1]+v[i])*(t[i]-t[i-1])
	s.append(sum/2)

#teiknar figurer

plt.title('Fart som funksjon av tid')
plt.plot(t, v, label = 'v(t)')
plt.grid()
plt.ylabel('fart')
plt.xlabel('tid')
plt.legend()

plt.figure()
plt.title('Akselerasjon som funksjon av tid')

plt.plot(t, a, label = 'a(t)')
plt.grid()
plt.ylabel('akselerasjon')
plt.xlabel('tid')
plt.legend()

plt.figure()
plt.title('Strekning som funksjon av tid')

plt.plot(t, s, label = 's(t)')
plt.grid()
plt.ylabel('strekning')
plt.xlabel('tid')
plt.legend()

plt.show()

"""
Terminal> python Oppgave_1.py

Her vert tre figurar teikna og vist av pyplot.
"""