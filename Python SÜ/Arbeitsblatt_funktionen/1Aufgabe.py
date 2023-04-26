def groesteZahl(zahlen):
    if zahlen[0] > zahlen[1] > zahlen[2]:
        return(zahl[0])
    if zahlen[1] > zahlen[0] > zahlen[2]:
        return(zahl[1])
    if zahlen[2] > zahlen[0] > zahlen[1]:
        return(zahl[2])

zahlen = input("Gib drei zahlen ein mit Beistrichen getrennt: ")
zahlen = zahlen.split(",")
groesteZahl(zahlen)
