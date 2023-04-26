'''
Programm, welches zufällige Zahlen von 1 bin 100 generiert und in eine CSV-Datei schreibt.
Maximilian
28.03.20023
'''

import random


#Erstellen der CSV-Datei
file = open("Spalten.txt" , "a")


#Erstellen der Werte, welche in die CSV-Datei geschrieben werden sollen
def werte():
    zeilen = ("wert1" , "wert2" , "wert3" , "wert4" , "wert5")
    for wort in zeilen:
        werteliste = []
        for wert in range(5):
            werteliste.append(random.randint(1,100))
    return werteliste


#Schreiben der Spalten und Zeilen in die CSV-Datei
spalten = ["Spalte 1", "Spalte 2", "Spalte 3" , "Spalte 4" , "Spalte 5"]
zeilen = []


#Hinzufügen der Spalten und Zeilen
for wort in spalten:
    file.write(wort + ";")

for a in range (10):
    zeilen.append(werte())
    #print(zeilen)
    #print (werte())

for z in zeilen:
    file.write("\n")
    for wert in z:
        file.write(str(wert) + ";")
