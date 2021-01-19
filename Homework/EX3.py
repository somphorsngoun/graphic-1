Array2D = eval(input())
integer = 0
sum = 0
for number in Array2D:
    for i in number:
        integer += i
        sum +=1
integer = integer/sum
print(int(integer))


arr = [ [2,3,4],
        [2,3,5],
        [4,5,6]
    ]
arr[0][2]