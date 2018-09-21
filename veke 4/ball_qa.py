"""
Exercise 4.9: Prompt the user for input to a formula
"""

g = 9.81

# program modified to take input for t and v0
# input is read as a string; we convert to float
t = float(input('t=? '))
v0 = float(input('v0=? '))

y = v0*t - 0.5*g*t**2
print ('%g' %(y))

"""
Terminal>   python ball_qa.py
t=? 0.6
v0=? 3
0.0342
"""
