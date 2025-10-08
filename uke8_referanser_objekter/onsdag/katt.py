class Katt:
    def __init__(self, navn, alder):
        self.navn = navn
        self.alder = alder
        self.eier = None
    
    def legg_til_eier(self, ny_eier):
        self.eier = ny_eier

    def mjau(self):
        print("mjauuuuu")

    def __str__(self):
        return f"{self.navn} {self.alder}"