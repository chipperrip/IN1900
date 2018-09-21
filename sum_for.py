"""
From the exercise collection:
Exercise 2.4. Errors in summation

s = 0; M = 3
for i in range(M):
    s += 1/2*k**2
print(s)

1)  The index of the loop is supposed to begin at 1

2)  The upper bound of the loop should be M+1

3)  The content of the loop doesn't use the index i.
    This isn't strictly necessary, but in this case
    we are trying to operate with the index in our
    summation formula, which leads to the following error:

4)  The variable k in s += 1/2*k**2 isn't initialised
    To rectify, the index should be k, not i

5)  The summation formula is wrong. k**2 is calculated
    before the division and multiplication, but we're
    supposed to exponentiate (2*k), not just k
"""

"""
I have included printouts from my loops to display that
they are working in the same way.
"""

# function sums all the values of (1/k)  for range k to M
def sum_for (k, M):
    #check for legal k value
    if(k <= 0 or M <=k ):
        print('Illegal k or M values in sum_while')
        return
        #variable for holding the sum
    s = 0
    print ('sum_for()')
    print ('  k   sum')
    print ('----------')
    #for loop for summation
    for k in range(k, (M+1)):

        s += 1/(2*k)**2
        print ('%3.0f %1.4f' %(k, s))

    print()
    return s

#while variant of the above
def sum_while (k, M):
    #check for legal k value
    if(k <= 0 or M <=k ):
        print('Illegal k or M values in sum_while()')
        return

    #variable for holding the sum
    s = 0
    print ('sum_while()')
    print ('  k   sum')
    print ('----------')
    #for loop for summation
    while k <= M:
        s += 1/(2*k)**2
        print ('%3.0f %1.4f' %(k, s))

        k += 1

    print ()
    return s

#test by comparing the sums of the for and while functions
def test_sums():
    computed = [sum_for (1, 20), sum_while (1, 20)]
    assert computed[0]==computed[1], 'sum_while() and sum_for() give differing results!'

test_sums()

"""
OUTPUT:
sum_for()
  k   sum
----------
  1 0.2500
  2 0.3125
  3 0.3403
  4 0.3559
  5 0.3659
  6 0.3728
  7 0.3779
  8 0.3819
  9 0.3849
 10 0.3874
 11 0.3895
 12 0.3912
 13 0.3927
 14 0.3940
 15 0.3951
 16 0.3961
 17 0.3970
 18 0.3977
 19 0.3984
 20 0.3990

sum_while()
  k   sum
----------
  1 0.2500
  2 0.3125
  3 0.3403
  4 0.3559
  5 0.3659
  6 0.3728
  7 0.3779
  8 0.3819
  9 0.3849
 10 0.3874
 11 0.3895
 12 0.3912
 13 0.3927
 14 0.3940
 15 0.3951
 16 0.3961
 17 0.3970
 18 0.3977
 19 0.3984
 20 0.3990
"""
