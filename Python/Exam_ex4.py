X = True
numberLess = 0
while X:
    number = int(input())
    if number <= 10:
        numberLess += number
    if numberLess == 20:
        print("WIN")
        X = False
    if numberLess > 20:
        print("LOST")
        X = False