infile = open('Fdeg.dat', 'r')

for i in range (3):
    infile.readline()

Fdegrees = []
Cdegrees = []

for line in infile:
    F = line.split()[-1]

    F = float(F)
    C = (F-32)*5.0/9
    Fdegrees.append(F)
    Cdegrees.append(C)

print (Fdegrees)
print (Cdegrees)

infile.close()

outfile = open('F2C.txt', 'w')

for F,C in zip(Fdegrees, Cdegrees):
    outfile.write('%4.2f %4.2f \n' %(C,F))

outfile.close()
