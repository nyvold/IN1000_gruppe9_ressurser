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
filnavn = "studenter.txt"
lesing(filnavn)
print("Mest populære linje er:")

def mest_poppis_linje(linjer):
    unike_linjer = set(linjer)
    storst = linjer.count(list(unike_linjer)[0])
    storst_linje = ""
    for linje in unike_linjer:
        antall = linjer.count(linje)
        if antall > storst:
            storst = antall
            storst_linje = linje
    return f"Den største linja er {storst_linje} med {storst} studenter"

print(mest_poppis_linje(linjer))