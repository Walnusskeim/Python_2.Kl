def pruefungpositiv(zahl):
    pruefung = True
    if zahl < 0:
        print("Zahl muss größer als null sein")
        pruefung = False
    else:
        print(zahl)
        pruefung = True
    return pruefung

while True:
    zahl = float(input("Gib eine Kommerzahl ein, welche Positiv ist: "))
    if pruefungpositiv(zahl) == False:
        continue
    else:
        break