
def lag_pizza(fyll, toppings):
    pizza = []
    pizza.append(fyll)
    pizza.extend(toppings)
    return pizza

inp1 = input("Ka slags fyll vil du ha?: ")
toppings = []
inp2 = []
inp2 = input("Ka slags toppings vil du ha? (0 for stopp): ")
while inp2 != "0":
    inp2 = input("Ka slags toppings vil du ha? (0 for stopp): ")
    toppings.append(inp2)

pizza = lag_pizza(inp1, inp2) # ['tomatsaus', ['ost', 'skinke']]
print(pizza)
