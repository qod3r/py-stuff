class SparseArray:
    def __init__(self):
        self.l = []
        self.idx = {}
    
    def __setitem__(self, k, v):
        self.idx[k] = len(self.l)
        self.l.append(v)
    
    def __getitem__(self, k):
        if k in self.idx:
            return self.l[self.idx[k]]
        else:
            return 0
    
    def print_inner(self):
        print(self.l)


arr = SparseArray()
arr[1] = 10
arr[8] = 20

for i in range(10):
    print(f"arr[{i}] = {arr[i]}")