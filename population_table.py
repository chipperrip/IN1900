"""
From the exercise collection:
Exercise 2.6. Table showing population growth
"""

from numpy import exp

#carrying capacity of the species in the environment
B = 50000

#Population 5000 at t= 0, find C
Nt0 = 5000
C = (B - Nt0)/Nt0

#number of time intervals
n = 48
#list of time intervals
t = [i for i in range(n+1)]

#constant k tells us how fast the population grows
k = 0.2

#Growth of a population by logistic function, stored in a list
N = [(B / (1+C*exp(-k*t[i]))) for i in range(n+1)]

print()

#present the lists in a table
for t, N in zip(t, N):
    print ('%2.0f h  %5.0f N' %(t, N))


"""
OUTPUT:

 0 h   5000 N
 1 h   5975 N
 2 h   7109 N
 3 h   8418 N
 4 h   9913 N
 5 h  11598 N
 6 h  13474 N
 7 h  15531 N
 8 h  17749 N
 9 h  20099 N
10 h  22543 N
11 h  25035 N
12 h  27526 N
13 h  29968 N
14 h  32315 N
15 h  34528 N
16 h  36580 N
17 h  38451 N
18 h  40131 N
19 h  41620 N
20 h  42924 N
21 h  44054 N
22 h  45025 N
23 h  45852 N
24 h  46552 N
25 h  47141 N
26 h  47635 N
27 h  48047 N
28 h  48390 N
29 h  48674 N
30 h  48909 N
31 h  49103 N
32 h  49263 N
33 h  49395 N
34 h  49504 N
35 h  49593 N
36 h  49666 N
37 h  49726 N
38 h  49776 N
39 h  49816 N
40 h  49849 N
41 h  49877 N
42 h  49899 N
43 h  49917 N
44 h  49932 N
45 h  49945 N
46 h  49955 N
47 h  49963 N
48 h  49970 N
"""
