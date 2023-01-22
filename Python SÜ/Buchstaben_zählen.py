'''
Ein Programm welches die Länge eines Strings bestimmt
Maximilian
22.01.2023
'''
import time    #Modul time importieren

#Fragt den Nutzer nach einem String
x = input('Gib einen Text mit Buchstaben, Leerzeichen, Sonderzeichen und Zahlen ein: ')


#Funktion, welche die Länge des Strings bestimmt
def count_letters(x):
    letters = 0
    for i in x:             #sieht sich jedes Zeichen an
        if i.isalpha():     #Wenn Buchstabe
            letters += 1    #Zähler um 1 erhöhen
    return letters

#Funktion welche alle buchstaben in eine Liste speichert
def letters_in_list(x):
    anzahl = []
    for i in x:
        if i.isalpha():
            anzahl.append(i)      #wenn es ein Buchstabe ist, wird er in die Liste hinzugefügt
    return anzahl


print('Deine Eingabe hat genau', count_letters(x), 'Buchstaben!')     #Ausgabe der Anzahl der Buchstaben
time.sleep(1)


while True:
    frage = input('Möchtest du die Buchstaben sehen? (j/n) ')  # Frage, ob der Benutzer die Buchstaben sehen möchte

    if frage == 'j':        #Wenn der Benutzer 'j' eingibt, dann werden die Buchstaben ausgegeben
        print(letters_in_list(x))
        break

    elif frage == 'n':    #Wenn der Benutzer 'n' eingibt, dann wird die Ausgabe abgebrochen
        print('Okay, dann nicht. Tschüssi :)')
        break

    else:               #Wenn der Benutzer etwas anderes als 'j' oder 'n' eingibt, wird die Ausgabe abgebrochen
        print('Du hast keine gültige Eingabe getätigt!')
        continue



