from kategori import Kategori
class Garderobe:
    def __init__(self):
        self.kategorier = {} # <str, Kategori>
        self.antrekk = []
    
    def nytt_plagg(self, kategorinavn, farger):
        if kategorinavn not in self.kategorier:
            self.kategorier[kategorinavn] = Kategori(kategorinavn)
        self.kategorier[kategorinavn].nytt_plagg(farger)