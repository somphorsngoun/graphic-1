
array = eval(input())
newArray = []
for dictionary in array:
    if dictionary["price"] < 20:
        newArray.append(dictionary["name"])
print(newArray)