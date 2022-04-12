class Summator: 
    def transform(self, n):
        return n
    
    def sum(self, n):
        s = 0
        for i in range(1, n + 1):
            s += self.transform(i)
        return s


class PowerSummator(Summator):
    def __init__(self, b):
        self.b = b
    
    def transform(self, n):
        return n ** self.b


class SquareSum(PowerSummator):
    def __init__(self):
        super().__init__(2)
    
    
class CubeSum(PowerSummator):
    def __init__(self):
        super().__init__(3)

a = Summator()
b = SquareSum()
c = CubeSum()

print(a.sum(3))
print(b.sum(3))
print(c.sum(3))