class Onske:
    def __init__(self, beskrivelse, antall, min_pris):
        self._beskrivelse = beskrivelse
        self.antall = antall
        self.min_pris = min_pris

    def passer(self, max_pris):
        return self.min_pris <= max_pris
    
    def hent_beskrivelse(self):
        return self.beskrivelse
    
    def hent_minpris(self):
        return self.min_pris
    
    def __str__(self):
        return self.beskrivelse + " Pris: " + self.min_pris

    def __eq__(self, other):
        return self.beskrivelse == other.beskrivelse
