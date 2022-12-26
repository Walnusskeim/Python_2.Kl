'''
Basic Flip a coin
Maximilian
26.12.2022
'''

import random
import time

def coin_flip ():
    coin_toss = random.randint(0, 1000)
    print("Flipping the coin...")
    time.sleep(2)
    if coin_toss > 500:
        print("Heads!")
    else:
        print("Tails!")

    if coin_toss == 500:
        print("It landed on the edge lol")

    time.sleep(1)

while (True):
    a = input("Do you want to flip again? y/n \n")

    if a == "y":
        coin_flip()
    elif a == "n":
        print("Tschüssi!")
        break
    else:
        print("U fockin' twat type y OR n!")


