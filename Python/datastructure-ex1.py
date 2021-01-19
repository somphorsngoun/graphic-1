students = [
    ["Bunthoeun", 98],
    ["Sophea", 95],
    ["Dyna", 25],
    ["Chanthy", 60],
]
bestStudents = []
goodStudents = []
for i in range(len(students)):
    if students[i][1] > 75:
        bestStudents.append(students[i])
    else:
        goodStudents.append(students[i])
print("Best students : ", bestStudents)
print("Good students : ", goodStudents)