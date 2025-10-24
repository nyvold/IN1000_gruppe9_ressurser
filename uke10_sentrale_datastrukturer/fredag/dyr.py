class Dyr:
    def __init__(self, navn, art, alder, vekt):
        self.navn = navn
        self.art = art
        self.alder = alder
        self.vekt = vekt
    
    def lag_lyd(self):
        if self.art.lower() == "løve":
            print("løven brøler")
        elif self.art.lower() == "ape":
            print("apen skriker")
        elif self.art.lower() == "elefant":
            print("elefanten tramper")
    
    def __str__(self):
        return f"{self.navn} er en {self.art}, {self.alder} år gammel og veier {self.vekt}kg"