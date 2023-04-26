'''
Programm, welches mit dictionarys die Fehlstunden von Schülern zählt.
Maximilian
14.03.2023
'''

schueler = {}

def wochentage():
    tage = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag']
    for i in tage:
        try:
            print(f'Gib die Fehlstunden für {i} ein (Die Namen bzw. Fehlstunden mit Beistrichen trennen, mit "break" abbrechen):')
            fehlstunden = {}
            name = input("Name: ")
            fehlstunden = input("Fehlstunden: ")
            if name == 'break' or fehlstunden == 'break':
                break
            else:
                name = name.split(',')
                fehlstunden = fehlstunden.split(',')
                fehlstunden = [int(i) for i in fehlstunden]
                for i in range(len(name)):
                    if name[i] in schueler:
                        schueler[name[i]] += fehlstunden[i]
                    else:
                        schueler[name[i]] = fehlstunden[i]
        except ValueError:
            print("Bitte gib nur Zahlen ein!")
            break
        except IndexError:
            print("Sieht aus als hättest du zu viele Namen oder Fehlstunden eingegeben!")
            break

while True:
    wochentage()
    print("Willst du noch einen Schüler eintragen? (j/n)")
    eingabe = input()
    if eingabe == 'j':
        continue
    elif eingabe == 'n':
        print("Schüler: Fehlstunden")
        for s in schueler:
            print(f'{s}: {schueler[s]} Stunden')
        break