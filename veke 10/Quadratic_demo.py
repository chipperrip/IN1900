"""
Frå boka:

Exercise 7.5: Make a class for quadratic functions

Denne fila er til demonstrasjon av Quadratic.py
"""

from Quadratic import Quadratic

print('\nWe are demonstrating the Quadratic class/module:')

print('Table demonstration:')
Quadratic.table_demo()

print('value() test:')
Quadratic.test_value()

print('roots() test:')
Quadratic.test_roots()

print('tests completed successfully')

"""
Terminal> python Quadratic_demo.py

We are demonstrating the Quadratic class/module:
Table demonstration:
           x     |     y
         -10          153
          -9          120
          -8           91
          -7           66
          -6           45
          -5           28
          -4           15
          -3            6
          -2            1
          -1            0
           0            3
           1           10
           2           21
           3           36
           4           55
           5           78
           6          105
           7          136
           8          171
           9          210
          10          253

value() test:
roots() test:
tests completed successfully
"""