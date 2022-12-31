'''
Einfacher Wärungsumrechner
Maximilan
30.12.2022
'''

#Funktionen
def eur_dollar(eingabe):
    dollar_ergebnis = eingabe * 1.075
    return dollar_ergebnis

def eur_yen(eingabe):
    yen_ergebnis = eingabe * 140.26
    return yen_ergebnis

def dollar_yen(eingabe):
    japyen_ergebnis = eingabe *140.26
    return japyen_ergebnis

def dollar_eur(eingabe):
    euro_ergebnis = eingabe / 1.075
    return euro_ergebnis

def yen_eur(eingabe):
    eur_ergebnis = eingabe / 140.26
    return eur_ergebnis

def yen_dollar(eingabe):
    amdollar_ergebnis = eingabe / 140.26
    return amdollar_ergebnis


####main####
def main ():
    print("###########WÄhRUNGSRECHNER###########")
    print("Welche Währung willst du umrechnen?")
    a = input(" 1 für Euro \n 2 für Dollar \n 3 für Yen \n")

    if a == "1":
        eingabe = float(input("Wie viel Euro willst du umrechnen? \n"))
    elif a == "2":
        eingabe = float(input("Wie viel Dollar willst du umrechnen? \n"))
    elif a == "3":
        eingabe = float(input("Wie viel Yen willst du umrechnen? \n "))
    else:
        print("Du hast keine der vorgegebenen Zahlen eingegeben loser!")

    # Nach ausgabe fragen
    print("In welche Währung willst du umrechnen?")
    ausgabe = float(input("1 für Euro , 2 für Dollar, 3 für Japanische Yen: \n"))

    if ausgabe == 1 and a == "1":
        print("Du hast schon Euro eingegeben!")
    elif ausgabe == 1 and a == "2":
        ergebnis = dollar_eur(eingabe)
        print(ergebnis)
    elif ausgabe == 1 and a == "3":
        ergebnis = yen_eur(eingabe)
        print(ergebnis)
    elif ausgabe == 2 and a == "1":
        ergebnis = eur_dollar(eingabe)
        print(ergebnis)
    elif ausgabe == 2 and a == "2":
        print("Du hast schon Dollar eingegeben!")
    elif ausgabe == 2 and a == "3":
        ergebnis = yen_dollar(eingabe)
        print(ergebnis)
    elif ausgabe == 3 and a == "1":
        ergebnis = eur_yen(eingabe)
        print(ergebnis)
    elif ausgabe == 3 and a == "2":
        ergebnis = dollar_yen(eingabe)
        print(ergebnis)
    elif ausgabe == 3 and a == "3":
        print("Du hast schon Yen eingegeben!")
    else:
        print("Du hast keine der vorgegebenen Zahlen eingegeben loser!")

nochmal = input("Willst du nochmal umrechnen? y/n \n")
if nochmal == "y":
    main()
elif nochmal == "n":
    print("Tschüssi!")