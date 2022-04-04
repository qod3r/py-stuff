class Balance:
    def __init__(self):
        self.right, self.left = 0, 0
    
    def add_right(self, n):
        self.right += n
        
    def add_left(self, n):
        self.left += n
    
    def result(self):
        if self.right > self.left:
            return "R"
        elif self.right < self.left:
            return "L"
        else:
            return "="


balance = Balance()
balance.add_right(10)
balance.add_left(5)
balance.add_left(5)
print(balance.result())
balance.add_left(1)
print(balance.result())