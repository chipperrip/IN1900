"""
Frå fysikkheftet:

Oppgåve 6.2 - Lese og bruke fysiske konstanter
"""
# dictionary for konstanter
cd = {}

# a)
with open('physics_constants.dat', 'r') as infile:

    for line in infile:

        words  = line.split()

        symbol = words[-3].strip()
        value  = float(words[-2].strip())

        cd[symbol] = value

# b)
En = (cd['ke']**2*cd['me']*cd['e']**4) / (2*cd['hbar']**2)

print (En)

"""
Terminal>   python constants_hydrogen.py
            2.1798723086817252e-18

Dette er tilnærma lik 2.18 × 10**−18 J, slik oppgåva ville ha det
"""