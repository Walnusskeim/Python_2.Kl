'''
Beispiel Nr. 7
Maximilian
25.12.2022
'''

#Beispiel 1
fahrzeug1 = ["VW", "Golf", 2010, 5000]
fahrzeug2 = ["BMW", "3er", 2015, 6000]
fahrzeug3 = ["Audi", "A4", 2017, 25000]

budget = int(input("Gib dein maximales Budget ein: "))

if budget >= fahrzeug3[3]:
    print("Du kannst dir einen", fahrzeug3[0], fahrzeug3[1], "leisten.")
elif budget >= fahrzeug2[3]:
    print("Du kannst dir einen", fahrzeug2[0], fahrzeug2[1], "leisten.")
elif budget >= fahrzeug1[3]:
    print("Du kannst dir einen", fahrzeug1[0], fahrzeug1[1], "leisten.")
else:
    print("Du kannst dir leider kein Auto leisten.")

#Beispiel 2

counter = 0

a = int(input("Was ist 5+ 5? "))
if a == 10:
    print("Richtig!")
    counter = counter + 1

b = int(input("Was ist 5- 5? "))
if b == 0:
    print("Richtig!")
    counter = counter + 1

c = int(input("Was ist 5* 5? "))
if c == 25:
    print("Richtig!")
    counter = counter + 1

d = int(input("Was ist 5/ 5? "))
if d == 1:
    print("Richtig!")
    counter = counter + 1

e = int(input("Was ist 5% 5? "))
if e == 0:
    print("Richtig!")
    counter = counter + 1

if counter == 0:
    print("Du hast alle Fragen falsch beantwortet!")
elif counter == 1 or counter == 2:
    print("Viele Fehler: weitere Übung erforderlich")
elif counter == 3 or counter == 4:
    print("Gute Leistung")
elif counter == 5:
    print("Super! Alle Aufgaben richtig gelöst!")
