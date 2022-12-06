'''
Einührung in Prozeduren und Funktionen
Autor: Alexander Jäger
Datum: 20.10.2021
'''

# Eingabe der 1. Zahl. Diese muss größer als 0 sein
def input_positive_numer ():
    z1 = 0
    while z1 <= 0:
       z1 = int(input("Zahl: "))
       if z1 <= 0:
            print("Die Zahl muss groesser als 0 sein!")
    return z1

z1 = input_positive_numer()
z2 = input_positive_numer()

# Berechnung des größten gemeinsamen Teilers
while z2 != 0:
    if z1 > z2:
        z1 = z1 - z2
    else:
        z2 = z2 - z1

# Ausgabe des größten gemeinsamen Teilers
print('Der größte gemeinsame Teiler ist ' + str(z1))
