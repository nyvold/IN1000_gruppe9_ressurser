from bur import Bur

class Seksjon:
    def __init__(self, navn, rader, kolonner):
        self.navn = navn
        self.rutenett = []
        for r in range(rader):
            rad = []
            for k in range(kolonner):
                bur = Bur(f"{r}-{k}")
                rad.append(bur)
            self.rutenett.append(rad)
    
    def finn_dyr(self, navn):
        for rad in self.rutenett:
            for bur in rad:
                for dyr in bur.dyr:
                    if dyr.navn.lower() == navn.lower():
                        return bur
        return None

    def vis_alle_dyr(self):
        print(f"Seksjon: {self.navn}")
        for rad in self.rutenett:
            for bur in rad:
                print(bur)
    
    def hent_bur(self, rad, kolonne):
        if 0 <= rad <= len(self.rutenett) and 0 <= kolonne <= len(self.rutenett[0]):
            return self.rutenett[rad][kolonne]
        else:
            return None
        
    