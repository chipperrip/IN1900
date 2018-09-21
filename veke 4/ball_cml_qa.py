"""
Exercise 4.11: Use exceptions to handle wrong input

The program from Exercise 4.10 reads input from the command line.
Extend that program with exception handling such that missing
command-line arguments are detected. In the except IndexError block,
use the raw_input function to ask the user for missing input data.
"""

import sys

g = 9.81

# program modified to assign t, v0 to cml args
# args are strings; convert to floats
try :
    t, v0 = [float(x) for x in sys.argv[1:]]

except:
    print('Arguments not supplied, please input: ')
    t = float(input('t=? '))
    v0 = float(input('v0=? '))

y = v0*t - 0.5*g*t**2
print ('%g' %(y))

"""
Terminal>   python ball_cml.py 0.6 3
0.0342
"""
