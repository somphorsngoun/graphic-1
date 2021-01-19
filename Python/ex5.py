def getHospitalForNewPatient(maxBedsPerHospital, persons):
    # Your function code here !
    for i in maxBedsPerHospital:
        if maxBedsPerHospital[i] == len(personnsPerHospital[i]):
            return i
    return None


# MAIN
persons = eval(input())
maxBedsPerHospital = eval(input())
personnsPerHospital = {}


# Your main code here !
for n in maxBedsPerHospital:
    personnsPerHospital[n] = []

for r in persons:
    if personnsPerHospital[getHospitalForNewPatient(maxBedsPerHospital,personnsPerHospital)]=="None":
        personnsPerHospital[getHospitalForNewPatient(maxBedsPerHospital,personnsPerHospital)].append(r)

print(personnsPerHospital)