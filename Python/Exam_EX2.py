studentsData = eval(input())
name = ""
X = 0
if len(studentsData) == 0:
    print("No result")
else:
    Z = 0
    for dic in studentsData:
        if dic["score"] > Z:
            name = dic["name"]
            Z = dic["score"]

        if dic["score"] >= 75:
            X += 1

    print("The best student is",name)
    if X == len(studentsData):
        print("All students have more than 75")
