class Antrekk:
    def __init__(self, plagg, anledning):
        self.plagg = plagg
        self.anledninger = [anledning]
        for plagg in self.plagg:
            plagg.oppdater_ant_antrekk(1)
        
    def hent_plaggene(self):
        return self.plagg
    
    def legg_til_anledning(self, anledning):
        self.anledninger.append(anledning)
    
    def passer_til(self, anledning):
        return anledning in self.anledninger
    
    def har_farge(self, farge):
        for plagg in self.plagg:
            if plagg.har_farge(farge):
                return True
        return False