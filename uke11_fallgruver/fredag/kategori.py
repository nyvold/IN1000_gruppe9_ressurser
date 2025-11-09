from plagg import Plagg
from random import randint
class Kategori:
    def __init__(self, kategorinavn):
        self.navn = kategorinavn
        self.plagg = []
    
    def nytt_plagg(self, farger):
        nytt_plagg = Plagg(farger)
        self.plagg.append(nytt_plagg)
    
    def finn_plagg_med_farge(self, farge):
        plagg_liste = []
        for plagg in self.plagg:
            if plagg.har_farge(farge):
                plagg_liste.append(plagg)
        return plagg_liste
    
    def trekk_tilfeldig_plagg(self, farge):
        plagg_liste = self.finn_plagg_med_farge(farge)
        if len(plagg_liste) == 0:
            return None
        tilfeldig_indeks = randint(0, len(plagg_liste) - 1)
        return plagg_liste[tilfeldig_indeks]
