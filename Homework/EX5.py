array = eval(input())
if array.index("X") == len(array)-1:
    print(array)
else:
    index = array.index("X")
    array.pop(index+1)
    array.insert(index,"0")
    print(array)