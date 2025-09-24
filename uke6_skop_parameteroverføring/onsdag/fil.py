
# antar listene er definert utfor funksjon
ordbok = {}


def lesing(filsti):
    with open(filsti) as fil:
        for linje in fil:
            linje = linje.split()#[navn, linje, trinn]
            ordbok[linje[0]] = linje[1]

lesing("studenter.txt")
print(ordbok)
for fornavn, linje in ordbok.items():
    if fornavn[0] == "a" or fornavn[0] == "A":
        print(fornavn)
        print(linje)
        print("------")
    
