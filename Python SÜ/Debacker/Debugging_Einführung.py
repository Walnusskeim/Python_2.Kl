def sum(a: int ,b: int) -> int: #damit signalisiert man das a bzw. b vom Datentyp integer sein MUSS | und der Ausgabewert soll auch ein int sein
    c = a + b
    return c


y: int = sum(7,3)
print(y)

z = sum("Ha", "llo")
print(z)

