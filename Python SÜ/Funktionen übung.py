def summieren(zahlen):
    result = 0
    for zahl in zahlen:
        result += zahl #wie result = result + zahl
    return result

def generierte_zufallszahlen(anzahl):
    result = []
    for index in anzahl:
        zufallszahl = random.randit(0,100)
        result.append(zufallszahl)
    return result

y = [1, 5, 7, 3, 9, 8]
summe = summieren(y)
print (summe)