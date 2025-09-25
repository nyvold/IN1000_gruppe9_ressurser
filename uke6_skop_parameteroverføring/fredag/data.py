

studenter = []


def lesing(filsti):
    with open(filsti) as fil:
        for linje in fil:
            linje = linje.split()#[navn, linje, trinn]
            studenter.append({"navn":linje[0], "linje":linje[1], "trinn":linje[2]})

lesing("studenter.txt")
print(studenter)    

    
