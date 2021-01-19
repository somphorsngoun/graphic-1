# TODO :
def sizeOfname(n1,n2):
    if len(name1) == len(name2):
        result = "same length"
    else:
        result = "different length"
    return "The length are… " + result
# - Remove the code DUPLICATION using a FUNCTION

# Test 1
name1 = "panha"
name2 = "ronan"

print(sizeOfname(name1,name2))
# Test 2
name3 = "rady"
name4 = "channak"

print(sizeOfname(name3, name4))
