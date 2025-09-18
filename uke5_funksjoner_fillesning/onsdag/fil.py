sti = "studenter.txt"
navn = []
linjer = []

with open(sti) as fil:
    for linje in fil:
        navnet, studie = linje.split()
        navn.append(navnet)
        linjer.append(studie)

print(navn)
print(linjer)
