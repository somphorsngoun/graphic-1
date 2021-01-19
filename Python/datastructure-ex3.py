print("Welcome to the student database")
print("0: exit")
print("1: add student to database with score 0")
print("2: add points to one student")
print("3: print student average")
print("4: print all students and score")
action = int(input("select an action : "))
students = []

while action != 0:
    if action == 1:
        # TODO :   - ask for the name of student, 
        #          - create a student with this name and with score=0 
        #          - append the new student to the students array
        Dic = {}
        Names = input()
        Dic["name"] = Names
        Dic["score"] = 0
        students.append(Dic)
        print(students)
    elif action == 2:
        # TODO :   - ask for the index of student, 
        #          - ask how many score to add
        #          - add score to the student in array
        Name = input()
        Score = int(input())
        students.append(Name)
        students.append(Score)
        print(students)
    elif action == 3:
        # TODO :   - calculate and print average score 
        Score = eval(input())
        sum = 0
        for n in range(len(Score)):
            sum += Score[n]["score"]
        average = sum/len(Score)
        print(average)
    elif action == 4:
        print(students)

    action = int(input("select an action : "))