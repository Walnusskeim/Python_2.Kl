while True:
    try:
        n = input("Bitte eine Ganzzahl (integer) eingeben: ")
        n = int(n)
        break
    except ValueError:
        print("Keine Integer! Bitte nochmals versuchen ...")
    except KeyboardInterrupt:
        print("Bist du blöd?! Nicht beenden min jung!")

print("Super! Das war's!")