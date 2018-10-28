"""
Frå boka:
Exercise 6.3: Use string operations to improve a program
"""


# tar ei liste av ord og set saman alle utenom det siste, med whitespace i mellom
def substance_a (words):
    return ' '.join(words[:-1])

# tar ein streng, separerer den om ein indeks, og returnerer verdiane på begge sider av lista
def substance_b (line):
    substance = line[:12].strip()
    density = float(line[12:])
    return substance, density

def test_substances():
    infile = open('densities.dat', 'r')
    densities_a = {}
    densities_b = {}

    for line in infile:
        #lagar verdiane for a
        words = line.split()
        densities_a[substance_a(words)] = float(words[-1])

        #verdiar for b
        s_d = substance_b(line)
        densities_b[s_d[0]] = s_d[1]

    assert densities_a == densities_b, 'The dictionaries are not equal!'

test_substances()

"""
Terminal > python density_improved.py

Ingen output, testen fungerer som den skal.

Eg er ikkje sikker på om eg har tydd oppgåva rett, men dersom ein
skulle ha to funksjonar på same form som density.py, har eg feiltolka den.

Det hadde uansett sett temmelig likt ut som testfunksjonen, berre for
kun ein dictionary om gangen.
"""
