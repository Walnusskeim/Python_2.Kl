def baumzeichnen(zeichen,zahl):
    while zahl >= 0:
        for z in range (0,zahl):
            print(zeichen, end="")
            zahl = zahl - 1

baumzeichnen("*",4)