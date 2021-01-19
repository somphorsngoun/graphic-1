teachers = [
    {"name": "jonathan", "brain": 75},
    {"name": "rady", "brain": 74},
    {"name": "hugo", "brain": 3},
    {"name": "ronan", "brain": 517},
    {"name": "edouard", "brain": -55},
]

# You code here !!!
result = []
for dictionary in teachers:
    if dictionary["brain"] > 60:
        result.append(dictionary["name"])

# Print : the name of teacher with a brain more than 60
print("Teacher very clever (a brain > 60) :",result)