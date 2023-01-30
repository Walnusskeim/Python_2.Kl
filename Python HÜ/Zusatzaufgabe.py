'''
Zusatzaufgabe zu der Übung "einfacher Währungsumrechner" Musterlösung
Maximilian
29.02.2023
'''

#Funktionen, welche das Umrechnen übernehmen
def usd(dollar):
    erg = dollar * 1.0869
    return erg

def yen(japyen):
    erg = japyen * 141.6500
    return erg


while True:
    #prüft, ob der Nutzer eine Fehleingabe getätigt hat
    try:
        print("-------------------------------------------------------------------------------")
        zahl = float(input("| In welche Währung willst du umrechnen? '1' für USD , '2' für Japanische Yen: "))  # hier wird die Währung ausgewählt
        print("-------------------------------------------------------------------------------")

        if zahl == 1:
            dollar = float(input("| Wie viele Euro willst du in Dollar umrechnen? "))
            print("-------------------------------------------------------------------------------")
            print(f"| Originale Eingabe: {dollar:^20.2f}€   | ", f" Umgerechnet in Dollar: {usd(dollar):^20.2f}$   | ") # hier wird die Funktion usd(dollar) aufgerufen
        elif zahl == 2:
            japyen = float(input("| Wie viel Euro willst du in Yen umrechnen? "))
            print("-------------------------------------------------------------------------------")
            print(f"| Originale Eingabe: {japyen:^20.2f}€   | ", f" Umgerechnet in Japnische Yen: {yen(japyen):^20.2f}$   | ")  # hier wird die Funktion yen(japyen) aufgerufen
        else:
            print("Keine gültige Zahl!")    # hier wird ausgegeben, wenn die Zahl nicht 1 oder 2 ist
            continue

        print("-------------------------------------------------------------------------------")
        break

    #wenn es ein ValueError ist
    except ValueError:
        print("---------------------------------------------------------------------")
        print("Du musst eine Zahl eingeben!")
        continue

    #Bei jedem anderen Error
    except:
        print("Unbekannter Error!")
        break