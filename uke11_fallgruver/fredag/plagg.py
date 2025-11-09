class Plagg:
    def __init__(self, farger):
        self.farger = farger
        self.antrekk = 0
    
    def har_farge(self, farge):
        return farge in self.farger
    
    def hent_ant_antrekk(self):
        return self.antrekk
    
    def oppdater_ant_antrekk(self, endring):
        self.antrekk += endring