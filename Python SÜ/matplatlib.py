import matplotlib.pyplot as plt

file = open("data.txt", "r")
daten = []
for line in file:
    line = line.strip("\n")
    daten.append(line.split("\t"))

x = []
y = []

for i in range(len(daten)):
    x.append(daten[i][0])
    y.append(daten[i][1])

plt.plot(x, y)
plt.show()
file.close()