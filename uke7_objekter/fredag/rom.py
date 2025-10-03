class Rom:
    def __init__(self, romnr, ant_senger, fasiliteter):
        self.romnr = romnr
        self.ant_senger = ant_senger
        self.fasiliteter = fasiliteter
        self.gjester = []
        self.reservert = False

    def reserver(self, nye_gjester):
        if self.reservert:
            #kun hvis self.reservert er True
            print(f"Beklager, rommet er allerede booket av {len(self.gjester)} gjester")
            return

        #kun hvis self.reservert er False
        for gjest in nye_gjester:
            self.gjester.append(gjest)
        self.reservert = True

    def hent_romnr(self):
        return self.romnr