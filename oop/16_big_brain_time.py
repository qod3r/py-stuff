from math import sqrt


class MathOps:
    def __init__(self):
        self.ops = dict()
        
        # pre-defined operations
        self.ops["x"] = Operation("x", "x", "identity", "")
        self.ops["sqrt_fun"] = Operation("sqrt_fun", "x", "sqrt", "")
    
    def add_operation(self, name, f1, op, f2):
        if name in self.ops.keys():
            print(f"Error: {op} already defined")
            return
        
        # convert string to actual Operation
        if f1 in self.ops.keys():
            f1 = self.ops[str(f1)]
        if f2 in self.ops.keys():
            f2 = self.ops[str(f2)]
        
        self.ops[name] = Operation(name, f1, op, f2)
    
    def perform(self, name, points):
        if name not in self.ops.keys():
            print(f"Error: {name} is not defined")
            return
        return list(map(self.ops[name], points))


class Operation:
    def __init__(self, name, f1, op, f2):
        self.name = name
        self.f1 = f1
        self.operator = op
        self.f2 = f2
    
    def __call__(self, x):
        if self.operator == "identity":
            return x
        elif self.operator == "sqrt":
            return sqrt(x)
        
        # TODO: this is mega bad
        # binary operators
        a = [0]
        if isinstance(self.f1, Operation) and isinstance(self.f2, Operation):
            exec(f"a[0] = self.f1({x}) {self.operator} self.f2({x})")
        elif isinstance(self.f1, Operation) and not isinstance(self.f2, Operation):
            exec(f"a[0] = self.f1({x}) {self.operator} float(self.f2)")
        elif not isinstance(self.f1, Operation) and isinstance(self.f2, Operation):
            exec(f"a[0] = float(self.f1) {self.operator} self.f2({x})")
        else:
            exec(f"a[0] = float(self.f1) {self.operator} float(self.f2)")
        
        return a[0]

    def __str__(self):
        return self.name
    

class OpParser:
    def __init__(self, aggregator):
        # binding
        self.aggregator = aggregator
    
    def parse(self, line):
        if line.split()[0] == "define":
            return self.__parse_def(line)
        elif line.split()[0] == "calculate":
            return self.__parse_calc(line)
        else:
            print("no commands recognized")
    
    def __parse_def(self, line):
        _, name, f1, op, f2 = line.split()
        self.aggregator.add_operation(name, f1, op, f2)
        return ""

    def __parse_calc(self, line):
        _, f, *points = line.split()
        points = list(map(float, points))
        return self.aggregator.perform(f, points)


if __name__ == "__main__":
    aggregator = MathOps()
    parser = OpParser(aggregator)

    for i in range(int(input())):
        print(parser.parse(input()))
    
    print("hey, as long as it works")