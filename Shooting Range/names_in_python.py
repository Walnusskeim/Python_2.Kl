names = ["Kaspar", "Umut", "Jeremias", "Elisabeth", "Bürsa"]
f = open("a.txt", "w")
for name in names:
    if "a" in name:
        f.write(name)
        f.write(", ")

f.close()
