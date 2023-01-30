'''
19 Fälle in mehreren Ländern analysieren

Autor: Maximilian Koch
Datum: 11.08.2022
'''

import matplotlib.pyplot as plt

#Erstellen der Listen

AUT = []
GER = []
CYP = []
BEL = []

#File wird geöffnet
file = open("time_series_covid19_confirmed_global.csv", "r")

# Importieren der Daten
for line in file:
    line = line.strip("\n")
    if "Austria" in line:
        AUT = line.split(",")
    elif "Germany" in line:
        GER = line.split(",")
    elif "Cyprus" in line:
        CYP = line.split(",")
    elif "Belgium" in line:
        BEL = line.split(",")

#File wird geschlossen
file.close()


#Die ersten vier Werte werden entfernt
for i in range(0,4):
    AUT.pop(0)
    GER.pop(0)
    CYP.pop(0)
    BEL.pop(0)

# Werte in float umwandeln
AUT = [float(i) for i in AUT]
GER = [float(i) for i in GER]
CYP = [float(i) for i in CYP]
BEL = [float(i) for i in BEL]


# diagramme
#Österreich
plt.title("Corona Österreich")
plt.plot(AUT, label="Austria")
plt.show()

#Deutschland
plt.title("Corona Deutschland")
plt.plot(GER, label="Germany")
plt.show()

#Zypern
plt.title("Corona Zypern")
plt.plot(CYP, label="Zypern")
plt.show()

#Berlgien
plt.title("Corona Belgien")
plt.plot(BEL, label="Belgien")
plt.show()

# Infektionen Österreichs werden in einer Datei gespeichert
file = open("austria.txt", "w")

# Alle Werte in der Liste durchgehen
for i in AUT:
    file.write(str(i) + "\n")

file.close()

print("Gesammtinfektionen Österreich:  {:.2f} Mio.".format(AUT[-1]))
