from string import ascii_lowercase
from string import ascii_uppercase
import random


def rndm_letter(groesse):
    zahl = random.randint(0,26)
    if groesse == "1":
        for x, y in zip(range(1,zahl), ascii_uppercase):
            print(y)
    else:
        for x, y in zip(range(1,zahl), ascii_lowercase):
            print(y)


groesse = input("'1' für großbuchstabe, '0' für kleinbuchstabe")
rndm_letter(groesse)