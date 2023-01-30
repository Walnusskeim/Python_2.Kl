'''
Ein einfacher Währungsumrechner. Musterlösung
Maximilian
29.01.2023
'''

#Funktion, die das Umrechnen übernimmt
def usd(zahl):
    erg = zahl * 1.0869
    return erg

while True:
    #prüft, ob der Nutzer eine Fehleingabe getätigt hat
    try:
        print("---------------------------------------------------------------------")
        zahl = float(input("| Wie viel Euro willst du in USD umrechnen? "))
        print("---------------------------------------------------------------------")
        print(f"|Originale Eingabe: {zahl:^20.2f}€   | " , f" Umgerechnet in Dollar: {usd(zahl):^20.2f}$   | ")
        print("---------------------------------------------------------------------")
        break
    #wenn es ein ValueError ist
    except ValueError:
        print("---------------------------------------------------------------------")
        print("Du musst eine Zahl eingeben!")
        continue
    #Bei jedem anderen Error
    except:
        print("Unbekannter Error!")
        continue
