
file = open("addresses.csv" , "r")

trennung = input('Gib das Trennungszeichen deiner Werte ein: ')

print(trennung)

werte = []
for line in file:
    x = line.strip('\n')
    x = x.split(trennung)
    for a in x:
        werte.append(a)

file.close()


for b in werte:
    try:
        b = int(a)
        print(f'{b:>20}' , ' |')
    except ValueError:
        try:
            b = float(a)
            print(f'{b:>20}', '| ')
        except ValueError:
            print(f'{b:<20}' , " | ")



print(werte)