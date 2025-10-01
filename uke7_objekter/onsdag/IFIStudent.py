# lag en ifi student med 3 metoder: 
from Fag import Fag

class IFIStudent:
    def __init__(self, navn, forening, linje):
        self.navn = navn
        self.forening = forening
        self.linje = linje
        self.fag = []
    
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
    
    # metode for å legge til en forening
    def legg_til_forening(self, ny_forening):
        if self.forening:
            if type(self.forening) == list:
                self.forening.append(ny_forening)
            else:
                foreninger = [self.forening]
                foreninger.append(ny_forening)
                self.forening = foreninger
        else:
            self.forening = []
            self.forening.append(ny_forening)




student1 = IFIStudent("Jonas", ["Navet", "MAPS"], "Prosa")
student2 = IFIStudent("Halvor", "Navet", "Prosa")
student3 = IFIStudent("Henning", None, "Robotikk")

print(student3.forening)
student3.legg_til_forening("Progsys")
print(student3.forening)


fag1 = Fag("5020", "Roman", "IN")
fag2 = Fag("5060", "Carsten", "IN")
fag3 = Fag("5320", "Terje", "IN")

student1.fag.extend([fag1, fag2, fag3])

for fag in student1.fag:
    print(fag.emnekode())

