"""
Exercise 2.2: Generate an approximate Fahrenheit-Celsius conversion table
"""

#C=-20
#dC= 5
F = 0
#change in F
dF = 10

while F<=100 :
    #convert F to C
    C = (F-32)*5/9
    #convert F to an approximate value of C
    aC = (F-30)/2
    print ('%3.0fF =%6.1fC ~%6.1fC' %(F,C,aC))
    #go to the next F value
    F = F+dF

"""
OUTPUT:
  0F = -17.8C ~ -15.0C
 10F = -12.2C ~ -10.0C
 20F =  -6.7C ~  -5.0C
 30F =  -1.1C ~   0.0C
 40F =   4.4C ~   5.0C
 50F =  10.0C ~  10.0C
 60F =  15.6C ~  15.0C
 70F =  21.1C ~  20.0C
 80F =  26.7C ~  25.0C
 90F =  32.2C ~  30.0C
100F =  37.8C ~  35.0C
"""
