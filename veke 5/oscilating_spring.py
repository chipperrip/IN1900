"""
Frå fysikkheftet:
Oppgave 5.5 - Oscillerende fjær

Hvis du henger en stein i enden av en fjær, trekker den ned en lengde A og slipper, vil steinen
oscillere opp og ned med en vertikal posisjon gitt etter formelen

y(t) = A*e**(-gamma*t)*cos(sqrt(k/m)*t)

Høyden y = 0 korresponderer til posisjonen steinen vil ha når den henger løst i fjæren.
Steinen har en masse m = 9 kg, og du trekker den ned en lengde A = 0.3 m. Sett k = 4 kg/s
2 og
γ = 0.15 s−1.
"""
import numpy as np
import matplotlib.pyplot as plt


def y_osc(t):
	A = -0.3 #m
	k = 4   #kg/s^2
	gamma = 0.15 #s^-1
	m = 9   #kg

	return A*np.e**(-gamma*t)*np.cos(np.sqrt(k/m)*t)


N = 100
index_set = range(N+1)

"""
a)
Lag to tomme arrays t_array og y_array av lengde 101. Bruk en for loop til å fylle dem med
tidsverdier i intervallet [0 s, 25 s], og korresponderende y(t) verdier


t_array = np.zeros(len(index_set))
y_array = np.zeros(len(index_set))

for i in index_set:
	t_array[i]=i*25/(N)
	y_array[i]=y_osc(t_array[i])

for t,y in zip(t_array, y_array):
	print ('%2.3f, %2.3f' %(t,y))
"""

"""
b)
Vektoriser koden ved bruk av numpy sin linspace funksjon, til å generere arrayet t_array, og
send den inn i en funksjon y(t) for å generere verdiene i y_array. Programmet ditt skal på dette
tidspunkt ikke inneholde noen loops.
"""

t_array = np.linspace(0, 25, 101)
y_array = y_osc(t_array)
for t,y in zip(t_array, y_array):
	print ('%2.3f, %2.3f' %(t,y))

plt.plot(t_array, y_array)

plt.show()