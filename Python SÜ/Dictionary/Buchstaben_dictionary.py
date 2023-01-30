'''
Programm, welches die Buchstaben einer Datei liest und jeden Buchstaben in ein Dictionary einträgt.
Das Dictionary wird dann in eine CSV Datei geschrieben, wenn es der Benutzer möchte.
Maximilian
30.01.2023
'''


import tkinter
from tkinter.filedialog import askopenfile
from tkinter import *
import time
import os

def get_file():
    while True:
        try:
            print("Bitte wähle eine Datei aus!")    #Frage, welche Datei der Benutzer auswählen möchte
            time.sleep(0.5)
            file = askopenfile(mode='r', filetypes=[('Text Files', '*.txt')])   #Öffnet die Datei
            return file
        except:
            print("Unbekannter Error!")    #Fehlermeldung, falls die Datei nicht geöffnet werden kann
            break

buchstaben = {"A": 0,"B": 0,"C": 0,"D": 0,"E": 0,"F": 0,"G": 0,"H": 0,"I": 0, "J": 0,"K": 0,"L": 0,"M": 0,  #Dictionary mit allen Buchstaben
            "N": 0,"O": 0,"P": 0,"Q": 0,"R": 0,"S": 0,"T": 0,"U": 0,"V": 0,"W": 0,"X": 0,"Y": 0,"Z": 0}

file = get_file()

for line in file:   #Zählt die Buchstaben in der Datei
    for char in line:
        if char.isalpha():  #und schreibt sie in das Dictionary
            buchstaben[char.upper()] += 1

file.close()

time.sleep(1)
print("Die Buchstaben wurden erfolgreich gezählt!")
time.sleep(2)
for key, value in buchstaben.items():   #Ausgabe des Dictionaries
    print(f"{key}: {value}" , end="       ")  #Ausgabe der Buchstaben und der Anzahl
    print(f"{round(value / sum(buchstaben.values()) * 100, 2)}%")   #Ausgabe der Prozentzahl
    print("------------------")

time.sleep(1)
frage = input("Möchtest du die Buchstaben in einer Datei speichern? (j/n)")  #Frage, ob der Benutzer die Buchstaben in einer Datei speichern möchte
frage = frage.lower()
if frage == "j":
    with open("buchstaben.txt", "w") as file:   #macht ein neues file names buchstaben.txt und schreibt die buchstaben und die Anzahl hinein
        for key, value in buchstaben.items():
            file.write(f"{key}: {value} {round(value / sum(buchstaben.values()) * 100, 2)}% \n")
            file.write("")
    path = os.path.realpath("buchstaben.txt")   #Die Variable path speichert den Pfad der Datei
    print(f"Die Datei wurde erfolgreich gespeichert! Sie befindet sich unter {path}")
elif frage == "n":
    print("Okay, dann nicht.")


#Zeile 36-39 Inspiration: Lucas Grundl, Code von GitHub