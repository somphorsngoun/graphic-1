# Enter your code here. Read input from STDIN. Print output to STDOUT
def countCharacter(text, character):
    number = 0
    for r in range(len(text)):
        if text[r] == character:
            number +=1
    if character == "a":
        return "a:"+str(number)
    elif character == "b":
        return "b:"+str(number)
    elif character == "c":
        return "c:"+str(number)
    elif character == "d":
        return "d:"+str(number)
    return number
        
String = input()

if "a" in String:
    print(countCharacter(String, "a"))
else:
    print("a:0")
if "b" in String:
    print(countCharacter(String, "b"))
else:
    print("b:0")
if "c" in String:
    print(countCharacter(String, "c"))
else:
    print("c:0")
if "d" in String:
    D = countCharacter(String, "d")
    print("d:",D)
else:
    print("d:0")
