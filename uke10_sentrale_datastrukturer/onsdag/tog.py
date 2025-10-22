from vogn import Vogn

class Tog:
    def __init__(self):
        self.forste = None
    
    def legg_til_vogn(self, navn):
        ny_vogn = Vogn(navn)
        # hvis lenkeliste er tom
        if self.forste is None: 
            self.forste = ny_vogn
        else:
            vogn = self.forste
            while vogn.neste is not None:
                vogn = vogn.neste
            vogn.neste = ny_vogn
    
    def __str__(self):
        s = ""
        vogn = self.forste
        print("Toget:")
        while vogn is not None:
            s += f"{vogn} -> "
            vogn = vogn.neste
        return s
        
tog = Tog()

v1 = Vogn("Gods 1")
v2 = Vogn("Gods 2")
v3 = Vogn("Gods 3")

tog.legg_til_vogn(v1)
tog.legg_til_vogn(v2)
tog.legg_til_vogn(v3)

print(tog)
        