"""
Frå fysikkheftet:

Oppgave 7.1 - Planet-klasse
"""
import numpy as np

class Planet:

	def __init__ (self, name, radius, mass, population):

		self.name = name
		self.radius = radius # in m
		self.mass = mass     # in kg
		self.population = population # in people

	def density (self):
		# D = M/V, V = 4/3 * pi * r**3
		return self.mass/((4/3)*np.pi*self.radius**3) # in kg/m^3

	def print_info (self):
		print()
		print('Planet info:')
		print('Name\t= '+self.name)
		print('Radius\t= %g m' %(self.radius))
		print('Mass\t= %g kg' %(self.mass))
		print('Density\t= %g kg/m^3' %(self.density()))
		print('Population = %g people' %(self.population))
		print()

planet1 = Planet('Earth', 6371000, 5.97237e24, 7497486172)

planet1.print_info()

print (planet1.name, "has a population of", planet1.population)

"""
Terminal python Planet.py

Planet info:
Name    = Earth
Radius  = 6.371e+06 m
Mass    = 5.97237e+24 kg
Density = 5513.6 kg/m^3
Population = 7.49749e+09 people

Earth has a population of 7497486172
"""