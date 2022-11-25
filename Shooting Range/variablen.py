names = "Nathan;Sebastian;Nicole;Sylvia;Daniel"
persons = names.split(";")
index = -1
for person in persons:
    index += 1
    if "Sebastian" == person:
        found = index + 1

if found > 0:
    print("Sebastian is at position", found)

