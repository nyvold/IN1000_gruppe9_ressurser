class Gruppe:
    # jeg antar krav refererer til ønskene til en gruppe med mennesker
    def __init__(self, krav):
        self.krav = krav # ["bad", "TV", "WIFI"]
        self.personer = []
    
    def hent_krav(self):
        return self.krav

    def hent_personer(self):
        return self.personer
