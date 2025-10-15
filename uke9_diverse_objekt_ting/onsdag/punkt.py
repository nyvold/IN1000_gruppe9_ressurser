class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p2 = Punkt(3, 3)
p3 = Punkt(3, 3)
print(p3.x == p2.x)

print(p2 is None)
