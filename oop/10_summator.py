class Summator: 
    def transform(self, n):
        return n
    
    def sum(self, n):
        s = 0
        for i in range(1, n + 1):
            s += self.transform(i)
        return s
    
    
class SquareSum(Summator):
    def transform(self, n):
        return n ** 2
    
    
class CubeSum(Summator):
    def transform(self, n):
        return n ** 3


a = Summator()
b = SquareSum()
c = CubeSum()

print(a.sum(3))
print(b.sum(3))
print(c.sum(3))

