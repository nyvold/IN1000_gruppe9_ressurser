# legge til liste
# poppe fra liste (fjerne)
# aksessere element
# sjekke om verdi er i en list
# string er en spesiell type liste

minListe = ["jonas", "per", "ivar"]

minListe.append("anakin")

print(minListe)

minListe.pop()

print(minListe)

navn = minListe[0]

print(minListe)

if "anakin" in minListe:
    print("spoiler: det e darth vader")

streng = "Laaaaang setning"
print(streng[3])