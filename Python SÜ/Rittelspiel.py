

import random
import time

tuer = random.randint(1,300)

def eins():
    if tuer <= 100:
        print("Du bist in einen Raum mit einem Drachen gekommen. Du hast verloren.")
    elif tuer > 100 and tuer <= 200:
        print("In dem Raum ist kein Drache du hast gewonnen.")
    elif tuer > 200 and tuer <= 300:
        print("In dem Raum ist kein Drache. Du hast gewonnen.")

#def zwei():
 #   if tuer <= 100:
  #      print("In dem Raum ist kein Drache. Du hast gewonnen.")
   # elif tuer > 100 and tuer <= 200:
    #    print("Du bist in einen Raum mit einem Drachen gekommen. Du hast verloren.")
    #elif tuer > 200 and tuer <= 300:
     #   print("In dem Raum ist kein Drache. Du hast gewonnen.")

#def drei():
 #   if tuer <= 100:
  #      print("In dem Raum ist kein Drache. Du hast gewonnen.")
   # elif tuer > 100 and tuer <= 200:
    #    print("In dem Raum ist kein Drache. Du hast gewonnen.")
    #elif tuer > 200 and tuer <= 300:
     #   print("Du bist in einen Raum mit einem Drachen gekommen. Du hast verloren.")

def abbruch():
    ebene = 1
    exit = False
    print("Willst du weitergehen? (j/n)")
    eingabe = input()
    if eingabe == "j":
        print("Dein Ritter geht durch die nächste Tür.")
        ebene = ebene + 1
        exit = False
    elif eingabe == "n":
        print("Du hast das Spiel abgebrochen und läufst davon. Peinlich.")
        print(f"Du hast {ebene} Level überlebt.")
        exit = True
    return exit

while True:
    print("Du steuerst einen Ritter durch ein Schloss. Es sind drei Türen vor dir. Welche wählst du?")

    eingabe = input()
    if eingabe == "1.Tür" or eingabe == "1" or eingabe == "1. tür":
        print("Du hast die erste Tür gewählt und öffnst sie...")
        time.sleep(2)
        eins()
        if abbruch() == False:
            continue
        else:
            break

    elif eingabe == "2.Tür" or eingabe == "2" or eingabe == "2. tür":
        print("Du hast die zweite Tür gewählt und öffnst sie...")
        time.sleep(2)
        eins()
        if abbruch() == False:
            continue
        else:
            break

    elif eingabe == "3.Tür" or eingabe == "3" or eingabe == "3. tür":
        print("Du hast die dritte Tür gewählt und öffnst sie...")
        time.sleep(2)
        eins()
        if abbruch() == False:
            continue
        else:
            break
