"""
Exercise 4.14: Evaluate a formula for data in a file

We consider the formula y(t)= v0*t-0.5*g*t**2 and want to 
evaluate y for a range of t values found in a file with format
"""
import random

"""
Oppgåve a)
"""
def ballinfo (file):

	infile = open(file,'r')
	data = infile.read()

	#splitter fila i segment
	data = data.split()

	#ut frå det vi veit om filformatet byrjar vi med å hente
	#det andre elementet.
	i = 1

	#vi hentar v0 verdien
	v0 = float(data[i])

	#hopp fram til t verdiane
	i = i + 2
	t = []

	#vi hentar t-verdiane inn i ei liste
	for j in range(i, len(data)):

		t.append(float(data[j]))


	infile.close()

	return v0, t

ballinfo_return = ballinfo('ball.dat')

print('\nOppgave a)\n')
print ('v0 = %g' %(ballinfo_return[0]))
print ('t values: ')

for t in ballinfo_return[1]:
	print(t)

"""
Oppgåve b)
"""
def test_ballinfo():
	filename = 'test.dat'
	outfile = open(filename,'w')
	"""
	generate a v0 value to be tested
	"""
	v0_expected = random.uniform(0,10)
	outfile.write('v0: %s\n' %(v0_expected))
	outfile.write('t:\n')

	t_expected = []

	"""
	generate t values to be tested
	"""
	for i in range (22):
		t_expected.append(random.uniform(0,10))
		outfile.write('%s ' %(t_expected[i]))

	outfile.close()

	# put our generated values through the ballinfo function
	computedList = ballinfo(filename)
	v0_result = computedList[0] == v0_expected
	t_result = computedList[1]

	#compare v0 values
	assert v0_result, 'v0 values do not match'

	#compare t values
	for i in range (22):
		assert t_result[i]==t_expected[i], 't values do not match'

test_ballinfo()

"""
Oppgåve c)

y(t) = v0*t-0.5*g*t**2, g = 9.81m/s^2

"""
def y(v0, t):
	return v0*t-(0.5*9.81*t**2)

def formatted_ty_file(v0, t_list):

	filename = 'formatted_ty.dat'
	outfile = open(filename, 'w')

	#litt pynt
	outfile.write('  t   |   y\n')

	#sorterar t verdiar i stigande rekkjefølgje
	t_list.sort()

	#reiknar ut tilhøyrande y verdiar
	for t in t_list:
		outfile.write('%1.3f | %2.3f\n'%(t, y(v0,t)))

	outfile.close()

#brukar infoen frå oppgåve a)
formatted_ty_file(ballinfo_return[0], ballinfo_return[1])


"""
Testen fungerer i b)

c) genererer eigen fil

TERMINAL> python ball_file_read_write.py

Oppgave a)

v0 = 3
t values:
0.15592
0.28075
0.36807889
0.35
0.57681501876
0.21342619
0.0519085
0.042
0.27
0.50620017
0.528
0.2094294
0.1117
0.53012
0.372985
0.39325246
0.21385894
0.3464815
0.57982969
0.10262264
0.29584013
0.17383923
"""