'''
Datenanalyse Landtagswahlen 1989, 1994, 1999, 2003, 2008, 2013, 2018 in Wörgl
Autor: Maximilian Koch
Datum: 24.10.2021
'''

# Importieren der Module
import matplotlib.pyplot as plt

def woergl(j):
    file = open(f"{j}.csv" , "r")
    woergl = []

    for line in file:
        if "Wörgl" in line:
            woergl = line.split(";")
    file.close()

    for a in range (0 , 10 , 1):
        woergl.pop(0)

    woergl = str(woergl)
    woergl = woergl.replace("," , ".")


    wahlbeteiligung = woergl[2:7]

    return wahlbeteiligung


jahre = [1989 , 1994 , 1999 , 2003 , 2008 , 2013 , 2018]
wahlbeteiligung = []

for j in jahre:
    wahlbeteiligung.append(woergl(j))

#print (wahlbeteiligung)
plt.title("Wahlbeteiligung in Wörgl", fontsize=20) # Titel
plt.ylim(0 , 50) # Y-Achse von 0 bis 100
plt.plot(jahre , wahlbeteiligung, label="Wahlbeteiligung") # Daten
plt.show() # Diagramm anzeigen


#print(woergl())