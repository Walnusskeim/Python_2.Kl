"""
Autor: Alexander JÃ¤ger
Datum: 6.2.2022
Analyseprogramm fÃ¼r SchÃ¼ler, zum Ãœben des Debuggens

Aufgabe:
* Programm debuggen
* Kommentare dazuschreiben
* Fehler ausbessern
* den Variablen cnt1 und cnt2 sinnvolle Namen geben
    #lettercount, nonlettercount
* In einem Satz erklÃ¤ren, was das Programm macht
    #Es zählt die Buchstaben und nicht-Buchstaben in einen, vom User eingegeben, Text.
* Ausgabe-Text in der letzten Zeile anpassen
* BegrÃ¼ÃŸungstext fÃ¼r Benutzer so anpassen, dass klar ist, was das Programm macht.
"""

print("Letter counter!")
text = ""
while len(text) < 5:
    text = input("Please enter a text phrase that is longer than 5 Characters:")
print("Thank you so much for this nice phrase!")

text = text.lower()
lettercount = 0
nonlettercount = 0
for letter in text:
    if letter in "abcdefghijklmnopqrstuvwxyzöäüß":
        lettercount = lettercount + 1
    else:
        nonlettercount = nonlettercount + 1

print(f"Your text has {lettercount} letters and {nonlettercount} special characters!")