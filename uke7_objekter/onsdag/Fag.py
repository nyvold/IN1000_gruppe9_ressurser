# lag en fag klasse, med emnenummer, faglærer, fagområde

class Fag:
    def __init__(self, emnenr, faglaerer, fagkode):
        self.emnenr = emnenr
        self.faglaerer = faglaerer
        self.fagkode = fagkode
    
    def emnekode(self):
        return self.fagkode + self.emnenr


fag1 = Fag("1000", "Siri", "IN")
fag2 = Fag("2040", "Lars", "IN")

print(fag1.emnekode())
print(fag2.emnekode())