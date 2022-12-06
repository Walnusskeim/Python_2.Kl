'''
Datenanalyse Landtagswahl 2018 in Imst
Autor: Maximilian Koch
Datum: 24.10.2021
'''

# Importieren der Module
import matplotlib.pyplot as plt

# Importieren der Daten
def import_woergl(file):
    file = open("2018.csv", "r")  #file wird geöffnet
    woergl = []   #liste wird erstellt

    for line in file:   #Wenn "Imst" gefunden wurde, splitten
        if "Wörgl" in line:
            woergl = line.split(";")
    file.close()    #file wieder schließen
    return woergl     #Wert wieder zurückgeben

#Importieren der Wahlbeteiligung
def import_wahlbeteiligung (woergl):
    print(woergl)
    for i in range(0, 10,1):    #Alle Dokumentationen bis "Wahlbeteiligung" werden gelöscht
        woergl.pop(0)
    print(woergl)
    wahlbeteiligung = woergl[0].replace(";", ".") #Strichpunkte werden zu Punkte
    return float(wahlbeteiligung)  #Zurückgeben des Wertes

wahljahre = [1989, 1994, 1999, 2003, 2008, 2013, 2018]  #Diese Variablen werden zum erstellen des Diagramms benötigt
wahlbeteiligung = []

for i in wahljahre:
    # fügt die wahlbeteiligung des jahres in die liste ein
    wahlbeteiligung.append(import_wahlbeteiligung(import_woergl("{}.csv".format(i))))


#Erstellen des Diagramms
plt.title("Wahlbeteiligung in Imst", fontsize=20) # Titel
plt.ylim(0, 100) # Y-Achse von 0 bis 100
plt.plot(jahre, wahlbeteiligung, label="Wahlbeteiligung") # Daten
plt.show() # Diagramm anzeigen