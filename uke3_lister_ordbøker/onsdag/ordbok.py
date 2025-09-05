# en dictionary med studenter, unike brukernavn 

phoneCountry = {"Norway":47, "Italy":39}

print(dict)

print(dict.keys()) #printer ut nøkler

print(dict.values()) #printer ut verdier

print(phoneCountry.get("Norway"))


studentDatabase = {"jonasbny":"Jonas Berger Nyvold", "jonber":"Jonas Berger Nyvold", "perio":"Per Danielsen", "ivar": "Ivar Ivarson"}
navn = studentDatabase.values()
brukernavn = studentDatabase.keys()
print(navn)
print(brukernavn)
