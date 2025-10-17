class Onske:
    def __init__(self, beskrivelse, antall, min_pris):
        self.beskrivelse = beskrivelse
        self.antall = antall
        self.min_pris = min_pris

    def passer(self, max_pris):
        return self.min_pris <= max_pris
    
    def __str__(self):
        return self.beskrivelse + " Pris: " + self.min_pris