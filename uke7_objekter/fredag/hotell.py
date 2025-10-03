from rom import Rom
class Hotell:
    def __init__(self, navn):
        self.navn = navn
        self.rom = {} # <romnr : Rom()>

rom1 = Rom(305, 2, ["wifi", "TV", "utsikt"])
rom2 = Rom(306, 2, ["wifi", "TV"])
rom3 = Rom(307, 3, ["wifi", "TV", "utsikt", "basseng"])

hotell = Hotell("IFI-hotellet")

ordbok = hotell.rom

ordbok[rom1.hent_romnr()] = rom1
ordbok[rom2.hent_romnr()] = rom2
ordbok[rom3.hent_romnr()] = rom3