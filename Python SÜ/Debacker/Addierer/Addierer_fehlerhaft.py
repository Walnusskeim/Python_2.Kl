'''Programm, das den Inhalt von 2 Listen analysiert.
Die erste Liste wird aus einer Datei gelesen.
Die zweite ist im Programm fixiert.
###Die zweite gibt der Benutzer ein.
'''


### Programm enthält 3 Fehler ###

# Funktionsdefinition
def sum_up(list1, list2):
    result = []
    # Anzahl der Elemente in den Listen bestimmen
    length1 = len(list1)
    length2 = len(list2)

    # die kürzere Liste mit 0 auffüllen
    if (length1 < length2):
        for counter in range(length2 - length1 - 1):
            list1.append(0)
    elif (length2 < length1):
        for counter in range(length2 - length1 - 1):
            list2.append(0)

    # Werte in den beiden (nun gleich langen Listen) aufsummieren
    for count in range(len(list1)):
        result.append(list1[count] + list2[count])
    # Ergebnisliste (mit Summen) in das Hauptprogramm zurÃ¼ck geben
    return result


#########################################################################
# Benutzerlisten definieren
user_list1 = []
user_list2 = []

# Dateiname einlesen
# filename = input("In welcher Datei sind Ihre Zahlen gespeichert?")
filename = "addierer_daten.txt"
# Datei Öffnen
fp = open(filename, "r")
# Zahlen einlesen
for line in fp:
    print(line)
user_list1.append(int(line))
# Datei schließen
fp.close()

# Zahlen vom Benutzer einlesen
# user_count = 0
# while(True):
#     user_input = (int(input("Ihre " + str(user_count + 1) + ". Zahl bitte:")))
#     if (user_input != 0):
#         user_list2.append(user_input)
#         user_count = user_count + 1
#     #Abbruch, sobald der Benutzer 0 eingibt
#     else:
#         break

# Zahlen von zweiter Liste direkt initialisiert
user_list2 = [10, 5, 7, 6, 9]

# Funktion mit den beiden Listen aufrufen
result_list = sum_up(user_list1, user_list2)
# Ergebnis der Analyse ausgeben
print("Maximum aus Ihrer Liste: ", max(result_list))
print("Minimum aus Ihrer Liste: ", min(result_list))
print("Mittelwert aus Ihrer Liste: ", sum(result_list) / len(result_list))
