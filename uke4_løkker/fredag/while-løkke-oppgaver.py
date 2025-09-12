# 1
time = 10
while time > -1:
    print(time)
    time -= 1
print("ferdig!")

# 2
summen = []
inp = input("Skriv inn tall (0 for stopp): ")
while inp != "0":
    summen.append(int(inp))
    inp = input("Skriv inn tall (0 for stopp): ")
print(sum(summen))

summen = 0
while True:
    inp = input("Skriv inn tall (0 for stopp): ")
    if inp == "0":
        break
    summen += int(inp)
print(summen)