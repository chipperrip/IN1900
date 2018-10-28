"""
Frå kjemiheftet:

Oppgave 5.5: Bjerrumplot

"""
import numpy as np
import matplotlib.pyplot as plt

#likevektskonstantar for reaksjonane CO2+H2O <-> H^+ + HCO3^- og HCO3^- <-> CO3^2-
K1 = 5.01e-7
K2 = 4.79e-11

pH = np.linspace(4,12,101)
print (pH)
# H^+ = 10**-pH, takk til den som la ut dette tipset på piazza

co2  = ((10**(-pH))**2) / ( ((10**(-pH))**2) + K1*10**(-pH) + K1*K2 )
hco3 =   (K1*10**(-pH)) / ( ((10**(-pH))**2) + K1*10**(-pH) + K1*K2 )
co3  =          (K1*K2) / ( ((10**(-pH))**2) + K1*10**(-pH) + K1*K2 )


#stygg tilnærming av skjæring mellom grafer

#to lister for å halde på skjæringspunkta
co2_x_hco3 = [[],[]]
hco3_x_co3 = [[],[]]

tol = 4e-2

#loop for å gå gjennom begge arrays, og få med seg index vidare,
#som vert brukt til å ta med riktig pH verdi i svaret.
for i, (a,b) in enumerate(zip(co2, hco3)):
	if abs(a-b)<tol and b>0.1:
		co2_x_hco3[0].append(pH[i])
		co2_x_hco3[1].append(a)

for j, (c,d) in enumerate(zip(hco3, co3)):
	if abs(c-d)<tol and c>0.1:
		hco3_x_co3[0].append(pH[j])
		hco3_x_co3[1].append(c)

#slutt på stygg tilnærming

plt.title('Bjerrumdiagram')

plt.plot(pH, co2, label='CO2(aq)')
plt.plot(pH, hco3, label='HCO3^-(aq)')
plt.plot(pH, co3, label='CO3^2-(aq)')

plt.plot(co2_x_hco3[0], co2_x_hco3[1], 'go')
plt.plot(hco3_x_co3[0], hco3_x_co3[1], 'ro')

plt.legend()

plt.xlabel('pH')
plt.ylabel('Konsentrasjonsforhold')
plt.grid()

plt.show()

"""
Terminal> python bjerrum_plot.py

Programmet produserer eit Bjerrumdiagram.
Eg er ikkje mykje til kjemikar, men diagrammet ser riktig ut.

b) Vi kan sjå på grafen at vi har eit skjæringspunk i 
om lag 6.3pH for co2_x_hco3, og om lag 10.3pH for hco3_x co3.

Eg har prøvd å lage ein stygg måte å finne skjæringspunktet, men
orkar ikkje bruke tid på å reikne på optimal inndeling av pH-verdiar
og toleranse for å treffe riktig. Dette er representert ved prikkar 
på diagrammet nær skjæringspunkta.

"""