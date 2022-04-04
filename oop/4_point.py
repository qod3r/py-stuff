class Point:
    def __init__(self, x, y):
        self.p = (x, y)
    
    def __eq__(self, other):
        return self.p == other.p

    def __ne__(self, other):
        return self.p != other.p


p1 = Point(1, 2)
p2 = Point(1, 2)

print(p1 == p2)
print(p1 != p2)
