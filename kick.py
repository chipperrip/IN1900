"""
Exercise 1.11: Compute the air resistance on a football
"""

from math import *
#density of the air
sigma = 1.2

#velocity of the football in m/s Vh for a hard 120km/h kick, Vs for a soft 30km/h kick
Vh = 120/3.6
Vs = 30/3.6

#mass of the football
m = 0.43

#Area of the football with radius a
a = 0.11
A = pi*a**2

#drag coefficient
Cd = 0.4

#Force of gravity
Fg = m*9.81

#compute the air resistance on a football kicked hard
FdHard = (1/2)*Cd*sigma*A*Vh**2

#compute the air resistance on a football kicked hard
FdSoft = (1/2)*Cd*sigma*A*Vs**2

#ratio of the drag force to the grav force for hard and soft kicks
FrHard = FdHard/Fg
FrSoft = FdSoft/Fg

print("\nFor a hard kick (120km/h), the drag force is %.1f N. The gravity force is %.1f N.\nThe ratio of the drag force and the gravity force is %.1f."%(FdHard,Fg, FrHard))

print("\nFor a soft kick ( 30km/h), the drag force is %.1f N. The gravity force is %.1f N.\nThe ratio of the drag force and the gravity force is %.1f.\n"%(FdSoft,Fg, FrSoft))

"""
OUTPUT:

For a hard kick (120km/h), the drag force is 10.1 N. The gravity force is 4.2 N.
The ratio of the drag force and the gravity force is 2.4.

For a soft kick ( 30km/h), the drag force is 0.6 N. The gravity force is 4.2 N.
The ratio of the drag force and the gravity force is 0.2.

"""
