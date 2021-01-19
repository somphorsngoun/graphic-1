
Boolean = True
sum = 0
while Boolean:
    number = int(input())
    if number == 72:
        print("Win")
        Boolean = False
    sum += 1
    if sum == 3:
        Boolean = False
        print("Lost")
    else:
        print("againt")