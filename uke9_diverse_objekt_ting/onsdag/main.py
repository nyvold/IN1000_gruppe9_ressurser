
from motor import Motor
from fleet import Fleet
from car import Car

m1 = Motor(150, 0, "Diesel")
m2 = Motor(250, 0, "Bensin")

c1 = Car("BMW", 1234, m2, "blå")
c2 = Car("BMW", 12345, m2, "rød")
c3 = Car("Volvo", 1224, m1, "blå")

f1 = Fleet("Bruktbilforhandler", 13)

f1.legg_til(c1)
f1.legg_til(c2)
f1.legg_til(c3)

print(f1)