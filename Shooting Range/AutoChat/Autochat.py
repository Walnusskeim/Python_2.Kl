'''
Ein Script, welches automatisch Nachrichten auf Snapchat.web verschickt.
Maximilian
21.05.2023
'''

import pyautogui
import time

paui = pyautogui

#Die Bildschirmgröße erfassen
screenWidth , screenHeight = paui.size()
print("Bildschirmgröße: " + str(screenWidth) + "Pixel x " + str(screenHeight) + "Pixel")

#Die aktuelle Position der Maus erfassen
currentMouseY , currentMouseX = paui.position()
print("Aktuelle Mausposition: " + str(currentMouseX) + " x " + str(currentMouseY))

#Bewegen der Maus auf das "Minimieren" Symbol und klicken
paui.moveTo(1775, 25)
paui.click()

#Bewegen der Maus auf das "Microsoft Edge" Symbol und klicken
paui.moveTo(950,970)
paui.doubleClick()
time.sleep(12)

#Maus auf die Suchleiste bewegen und klicken
paui.moveTo(400,60)
paui.click()

#Text eingeben
paui.typewrite("snapchat web")
paui.press("enter")
time.sleep(8)

#Auf den richtigen Link klicken
paui.moveTo(400, 355)
paui.click()
time.sleep(8)

#Einen Kontakt auswählen
paui.moveTo(325, 450) # +75 bei der letzten Zahl für den nächsten Kontakt (Bei 325, 375 befindet sich der 1. Kontakt)
paui.click()
time.sleep(8)

#Nachricht eingeben
paui.moveTo(1825, 1035)
paui.typewrite("Hallo Lea diese Nachricht wurde automatisch gesendet :)")
time.sleep(0.5)
paui.click()
time.sleep(5)
