students = [
    {
        "name": "Bunthoeun", 
        "score": 98
    },
    {
        "name": "Sophea", 
        "score": 95
    },
    {
        "name": "Dyna", 
        "score": -12
    },
    {
        "name": "Chanthy", 
        "score": 25
    },
]
bestStudents = []
goodStudents = []
for i in range(len(students)):
    studentsname = students[i]["name"]
    studentsScore = students[i]["score"]
    if studentsScore > 75:
        bestStudents.append(studentsname)
    else:
        goodStudents.append(studentsname)
print("Best students : ", bestStudents)
print("Good students : ", goodStudents)