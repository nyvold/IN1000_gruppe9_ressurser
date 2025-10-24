class Bur:
    def __init__(self, id):
        self.id = id
        self.dyr = []
    
    def legg_til_dyr(self, dyr):
        self.dyr.append(dyr)
    
    def fjern_dyr(self, navn):
        for dyr in self.dyr:
            if dyr.navn.lower() == navn.lower():
                self.dyr.remove(dyr)
                return
        print(f"Fant ikke dyr med navn {navn}")
    
    def tell_dyr(self):
        return len(self.dyr)
    
    def __str__(self):
        if self.tell_dyr() == 0:
            return "Buret er tomt"
        else:
            s = ""
            s += f"{self.id}"
            for dyr in self.dyr:
                s += f"{dyr} \n"
            return s