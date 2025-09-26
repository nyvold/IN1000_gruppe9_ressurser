studenter = []
def hent_studenter(filsti):
    with open(filsti) as fil:
        for linje in fil:
            linje = linje.split()
            student = {"navn":linje[0], "linje":linje[1], "trinn":linje[2]}
            studenter.append(student)
            

hent_studenter("studenter.txt")

def mest_populere_linje(studenter):
    # initialiserer variabler
    linjer = []
    populer_linje = ""
    storst = 0

    # lager liste med alle linjer
    for student in studenter:
        linjer.append(student["linje"])
    
    unike_linjer = set(linjer)# finner unike linjer

    # finner største linje
    for linje in unike_linjer:
        antall = linjer.count(linje) #finner antall studenter for en linje
        # print(linje)
        # print(antall)
        if antall > storst:
            storst = antall
            populer_linje = linje
    return populer_linje

def antall_forsteaar(populer_linje):
    antall_relevante_stud = 0
    # teller antall studenter som er 'linje' OG går første året
    for student in studenter:
        if student["linje"] == populer_linje and student["trinn"] == "1":
            antall_relevante_stud += 1
    return antall_relevante_stud
    

print(antall_forsteaar(mest_populere_linje(studenter)))
