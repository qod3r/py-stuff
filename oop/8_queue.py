class Queue:
    def __init__(self, *n):
        self.arr = list(n)

    def __str__(self):
        if len(self.arr) == 0:
            return "[]"
        res = "["
        for i in self.arr:
            if i == self.arr[len(self.arr) - 1]:
                res += f"{i}]"
            else:
                res += f"{i} -> "
        return res    
    
    def __add__(self, other):
        c = self.copy()
        c.extend(other)
        return c
    
    def __iadd__(self, other):
        self.extend(other)
        return self
        
    def __eq__(self, other):
        return self.arr == other.arr
    
    def __rshift__(self, N):
        if N > len(self.arr):
            return Queue()
        else:
            c = self.copy()
            for i in range(N):
                c.pop()
        return c
    
    def __next__(self):
        return self.next()
    
    def copy(self):
        return Queue(*self.arr)
    
    def next(self):
        self_copy = self.copy()
        self_copy.pop()
        return self_copy
        
    def append(self, *n):
        for i in list(n):
            self.arr.append(i)
    
    def pop(self):
        return self.arr.pop(0)
    
    def extend(self, other):
        for i in other.arr:
            self.append(i)


q1 = Queue(1, 2, 3)
q2 = Queue(4, 5)

q1 += q2

print(q1)
print(Queue(1, 2) == Queue(2, 3))
print(Queue(1, 2) == Queue(1, 2))

print(q1 >> 3)