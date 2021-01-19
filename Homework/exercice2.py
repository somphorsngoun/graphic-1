
modules = {
    "module1": ["math", "english", "design"],
    "module2": ["algo", "html"],
    "module3": ["java"]
}


# You code here !!!
nameOfsubject = []
for module in modules:
    for subject in modules[module]:
        nameOfsubject.append(subject)

# Print : all topics of module1, module2, module3
print("All topics are:"+"\n"+str(nameOfsubject))