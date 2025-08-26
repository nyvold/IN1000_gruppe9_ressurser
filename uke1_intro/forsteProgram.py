print("Skriv inn ditt fornavn")
navn = input()

print("Skriv inn din alder")
alder = int(input())

if alder > 0 and alder < 120:
    print(f"navn: {navn} \nalder: {alder}")
else:
    print("Ugyldig alder :(")
