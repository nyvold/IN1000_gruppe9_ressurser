x = 10

def ytre():
    x = 20
    def indre():
        x = 30
        print("Inne i indre:", x)
    indre()
    print("Inne i ytre:", x)

ytre()
print("Utenfor alle funksjoner:", x)

