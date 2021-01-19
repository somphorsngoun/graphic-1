input = [
{"name": "Bunthoeun", "score": 90},
{"name": "Kunthy", "score": 75},
{"name": "Sreymom", "score": 95}
]
bestStudent = ""
maxnumber = 0
# dO SOMETHING
for dictionary in input:
    if dictionary["score"] > maxnumber:
        bestStudent = dictionary["name"]
        maxnumber = dictionary["score"] 
# Print the result
print("The best student is " + bestStudent)