bookinger = [] #1
def book(navn, gjester):#2
    bookinger.append(navn+gjester)#8
    print("booking bekreftet")

print("Hei velkommen til restauranten!")#3
navn = input("hva er navnet ditt?")#4
antall_gjester = input("Hvor mange gjester?")#5
antall_gjester = int(antall_gjester)#6
book(navn, antall_gjester)#7