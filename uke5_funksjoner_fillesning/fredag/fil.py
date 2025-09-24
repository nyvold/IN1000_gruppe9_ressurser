
# antar listene er definert utfor funksjon
navn = []
linjer = []
trinn = []

def lesing(filsti):
    with open(filsti) as fil:
        for linje in fil:
            linje = linje.split()
            navn.append(linje[0])
            linjer.append(linje[1])
            trinn.append(linje[2])

lesing("studenter.txt")
print(navn)
print(linjer)
print(trinn)