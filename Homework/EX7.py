name = input()
listOfname = []
while name != "stop":
    if len(name) >= 5:
        listOfname.append(name)
    name = input()
print(listOfname)