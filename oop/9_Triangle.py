class Triangle:
    def __init__(self, *n):
        self.a = n[0]
        self.b = n[1]
        self.c = n[2]
    
    def perimeter(self):
        return self.a + self.b + self.c


class EquilateralTriangle(Triangle):
    def __init__(self, n):
        super().__init__(n, n, n)


t = Triangle(1, 2, 3)
t1 = EquilateralTriangle(2)

print(t.perimeter())
print(t1.perimeter())