
def opprett_bankkonto():
    print("Velkommen til megafet bank, opprett en konto")
    saldo = input("Skriv inn saldoen på konto")

    #1. kan ikke sette inn 0 kroner
    if int(saldo) == 0:
        print("Kan ikke opprette konto med ", saldo, "kr")

    #2. kan ikke sett inn mindre enn 0 kroner
    if int(saldo) < 0:
        print("fyyyyy, DET DER EKKE LOV")

opprett_bankkonto()
