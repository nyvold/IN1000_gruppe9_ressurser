# lag en ifi student med 3 metoder: 
# metode for å legge til en forening
# lag en fag klasse, med emnenummer, faglærer, fagområde

class IFIStudent:
    def __init__(self, navn, forening, linje, fav_databrus):
        self.navn = navn
        self.forening = forening
        self.linje = linje
        self.fav_databrus = fav_databrus
    
    # hent_forening:
    def hent_en_forening(self):
        if type(self.forening) == list:
            return self.forening[0]
        else:
            return self.forening

    # metode for å beregne favoritt pub
    def beregn_pub(self):
        if self.forening:
            if self.forening == "MAPS":
                return "HighBury Pub"
            elif self.forening == "Navet":
                return "Lawo T"
            elif self.forening == "Mikro":
                return "Mastermind"
        else:
            if self.linje == "Digøk":
                return "Lawo"
            else:
                return "Mastermind"



student1 = IFIStudent("Jonas", ["Navet", "MAPS"], "Prosa", "Monster peachberry")
student2 = IFIStudent("Halvor", "Navet", "Prosa", None)
student3 = IFIStudent("Henning", None, "Robotikk", "RedBull")

studenter = [student1, student2, student3]
puber = []

for student in studenter:
    pub = student.beregn_pub()
    puber.append(pub)

print(puber)
