from katt import Katt
class Eier:
    def __init__(self, navn, katter):
        self.navn = navn
        self.katter = []
        self.katter.extend(katter)
    
    def legg_til_katt(self, katt):
        self.katter.append(katt)

    def __str__(self):
        return f"{self.navn} {self.katter}"
    

katt1 = Katt("Pus", 3)
kattkopi = katt1

eier1 = Eier("Jonas", [katt1])

katt1.legg_til_eier(eier1)

kattkopi.alder = 10

print(katt1.alder)
print(kattkopi.alder)
print(katt1.eier.navn)
print(kattkopi.eier.navn)