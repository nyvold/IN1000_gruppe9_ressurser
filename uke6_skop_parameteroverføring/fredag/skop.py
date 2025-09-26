
x = 10

def ytre():
    x = 20
    def indre(y):
        x = y
        print("Inne i indre", x)
    indre(x)
    print("Inne i ytre", x)

ytre()
print("utenfor alle funksjoner", x)