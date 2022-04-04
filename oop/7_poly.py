class Polynomial:
    def __init__(self, coef):
        self.coef = coef;
        # print(self.coef)
        
    def __add__(self, other):
        res = self.coef.copy()
        if len(other.coef) >= len(self.coef):
            for i in range(len(self.coef)):
                res[i] += other.coef[i]
            map(res.append, other.coef[i+1:])
        elif len(other.coef) < len(self.coef):
            for i in range(len(other.coef)):
                res[i] += other.coef[i]
        return res
        
    def poly(self, x):
        res = 0
        for i, v in enumerate(self.coef):
            res += v * (x ** i)
        return res


a = Polynomial([-3, 2, 1])
b = Polynomial([3, 2, 1])

print(a + b)
print(a.poly(2))
