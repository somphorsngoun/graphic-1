ListOfname = eval(input())
name = ""
population = ListOfname[0]["population"]
for key in ListOfname:
    if population > key["population"]:
        population = key["population"]
        name = key["name"]
if len(ListOfname) ==1:
    print(ListOfname[0]["name"])
else:
    print(name)