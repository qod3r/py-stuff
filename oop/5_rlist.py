class ReversedList:
    def __init__(self, l):
        self.l = l
        self.l.reverse()
    
    def __getitem__(self, k):
        return self.l[k]
    
    def __len__(self):
        return len(self.l)


r = ReversedList([1, 2, 3])
print([r[i] for i in range(len(r))])